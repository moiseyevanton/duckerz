# Cryptography 🔐

Раздел с writeup-отчетами по криптографии на платформе [Duckerz](https://duckerz.ru/).

В этой категории обычно встречаются:
- классические шифры;
- кодировки и преобразования;
- анализ хешей;
- ошибки в реализации криптографии;
- восстановление ключей или исходных сообщений.

---

## Решенные задачи ✅

| Задача | Сложность | Описание | Ссылка |
|---|---|---|---|
| Брутфорс | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Расшифровка текста, зашифрованного сдвигом Цезаря | [Открыть](./Bruteforce/) |
| Обратимость | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ hex-строк и свойства обратимости XOR | [Открыть](./Reversibility/) |
| Полиглот | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ текста, записанного в нескольких форматах кодирования | [Открыть](./Polyglot/) |
| Смежный | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ скрипта шифрования и результата его работы | [Открыть](./Adjacent/) |
| Two Time Pad | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Атака на повторное использование ключа в One-Time Pad | [Открыть](./Two_Time_Pad/) |
| Базированная база | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Последовательное декодирование Base64, Base32 и ASCII-кодов | [Открыть](./base/) |
| Ни в чём не ошибся | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | RSA: автор напечатал `e + p` вместо `e` — утечка `p`, восстановление ключа и расшифровка | [Открыть](./singlemistake/) |
| Только RSA | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | RSA как OSINT: факторизация `n` через factordb.com (слабый ключ, неравные `p`,`q`) → сбор ключа и расшифровка | [Открыть](./RSAonly/) |
| Туда-сюда | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | XOR каждого символа с его индексом; XOR обратен сам себе → дешифр тем же алгоритмом | [Открыть](./Backandforth/) |

---

## Прогресс 📈

```text
9/20
```

---

Автор: **masquadd :)** ✍️
