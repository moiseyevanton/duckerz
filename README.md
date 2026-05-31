# DUCKERZ Writeups 🐤

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=F7B731&center=true&vCenter=true&width=900&lines=Практика+CTF+и+web+security;Изучение+уязвимостей+и+эксплуатации;HTTP+%7C+Crypto+%7C+Reverse+%7C+OSINT+%7C+PWN;Документирование+решений+и+своя+база+знаний" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-DUCKERZ-f7b731?style=for-the-badge" alt="Platform DUCKERZ" />
  <img src="https://img.shields.io/badge/Solved-14%2F165-2ecc71?style=for-the-badge" alt="Solved 14/165" />
  <img src="https://img.shields.io/badge/Progress-8.5%25-3498db?style=for-the-badge" alt="Progress 8.5%" />
</p>

Данный репозиторий содержит мои walkthrough/writeup-отчеты по задачам с платформы [Duckerz](https://duckerz.ru/).

---

## Платформа 🚩

https://duckerz.ru/

---

## Категории 🗂️

| Категория | Прогресс | Описание | Ссылка |
|---|---:|---|---|
| Steganography | 1/23 | Задачи на поиск скрытых данных в изображениях, файлах и метаданных | [Открыть](./steganography/) |
| Web | 3/33 | Задачи на анализ веб-приложений, HTTP, cookies, сессий и контроля доступа | [Открыть](./web/) |
| Reverse | 1/23 | Задачи на реверс-инжиниринг бинарных файлов и восстановление логики программ | [Открыть](./reverse/) |
| Misc | 0/15 | Разные задачи: нестандартная логика, кодировки, файлы и небольшие расследования | [Открыть](./misc/) |
| Cryptography | 6/20 | Задачи на шифры, кодировки, хеши и криптографические ошибки | [Открыть](./cryptography/) |
| OSINT | 0/15 | Задачи на поиск информации в открытых источниках и анализ цифровых следов | [Открыть](./osint/) |
| Forensics | 2/18 | Задачи на анализ файлов, дампов, трафика, артефактов и цифровых следов | [Открыть](./forensics/) |
| PWN | 0/10 | Задачи на эксплуатацию бинарных файлов, память и низкоуровневые уязвимости | [Открыть](./pwn/) |
| Hardware | 1/8 | Задачи на схемы, микроконтроллеры, железо и аппаратные артефакты | [Открыть](./hardware/) |

---

## Решенные задачи ✅

| Задача | Категория | Сложность | Описание | Ссылка |
|---|---|---|---|---|
| Брутфорс | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Расшифровка текста, зашифрованного сдвигом Цезаря | [Открыть](./cryptography/Bruteforce/) |
| Обратимость | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Восстановление флага через обратимость XOR и сокращение известных ключей | [Открыть](./cryptography/Reversibility/) |
| Полиглот | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Декодирование частей флага из hex, Unicode escape и Base64 | [Открыть](./cryptography/Polyglot/) |
| Смежный | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Обращение аффинного шифра через обратное число по модулю 26 | [Открыть](./cryptography/Adjacent/) |
| Two Time Pad | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Атака на повторное использование ключа в One-Time Pad через XOR | [Открыть](./cryptography/Two_Time_Pad/) |
| Базированная база | Cryptography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Последовательное декодирование Base64, Base32 и ASCII-кодов | [Открыть](./cryptography/base/) |
| Путь домой | Hardware | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Копирование значения с красного ключа-таблетки на синий через программатор KeyCopy | [Открыть](./hardware/Wayhome/) |
| Классное фото | Steganography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Визуальная LSB-стеганография в младшем бите синего канала PNG-изображения | [Открыть](./steganography/Coolphoto/) |
| Cookies with milk | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ cookie, base64-декодирование сессии и подмена роли пользователя для доступа к админ-панели | [Открыть](./web/Cookieswithmilk/) |
| Забытый пароль | Reverse | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ Python-скрипта с простой схемой преобразования байтов через ключ `ord()` | [Открыть](./reverse/Forgottenpassword/) |
| Логинатор | Forensics | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Извлечение флага из URL-запросов `/flag.php/<символ>` в дампе логов | [Открыть](./forensics/Loginator/) |
| Pincode | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Вход через `admin:admin` и перебор 4-значного PIN-кода с помощью Turbo Intruder | [Открыть](./web/Pincode/) |
| Простой API-сервер | Forensics | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск HTTP-запроса авторизации с `username=hacker` и URL-encoded флагом в pcapng-дампе | [Открыть](./forensics/simple_api/) |
| Web polygon | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Получение частей флага через разные HTTP-методы и GET-параметр на `/flag` | [Открыть](./web/webpolygon/) |

---

## Структура репозитория 🧭

```text
.
├── README.md
├── cryptography/
│   ├── Adjacent/
│   ├── Bruteforce/
│   ├── Polyglot/
│   ├── Reversibility/
│   ├── Two_Time_Pad/
│   └── base/
├── forensics/
│   ├── Loginator/
│   └── simple_api/
├── hardware/
│   └── Wayhome/
├── misc/
├── osint/
├── pwn/
├── reverse/
│   └── Forgottenpassword/
├── steganography/
│   └── Coolphoto/
└── web/
    ├── Cookieswithmilk/
    ├── Pincode/
    └── webpolygon/
```

Каждая категория содержит отдельный README со списком задач. Каждая задача лежит в своей папке и содержит подробный writeup:
- описание задачи;
- ход разведки;
- используемые команды;
- объяснение уязвимости или техники;
- процесс эксплуатации;
- найденный флаг.

---

Автор: **masquadd :)** ✍️
