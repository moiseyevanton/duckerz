# DUCKERZ Writeups 🐤

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&color=F7B731&center=true&vCenter=true&width=900&lines=CTF+practice+and+web+security;Vulnerability+research+and+exploitation;HTTP+%7C+Crypto+%7C+Reverse+%7C+OSINT+%7C+PWN;Writeups+and+personal+knowledge+base" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-DUCKERZ-f7b731?style=for-the-badge" alt="Platform DUCKERZ" />
  <img src="https://img.shields.io/badge/Solved-29%2F165-2ecc71?style=for-the-badge" alt="Solved 29/165" />
  <img src="https://img.shields.io/badge/Progress-17.6%25-3498db?style=for-the-badge" alt="Progress 17.6%" />
</p>

Данный репозиторий содержит мои walkthrough/writeup-отчеты по задачам с платформы [Duckerz](https://duckerz.ru/).


---

## Категории 🗂️

| Категория | Прогресс | Описание | Ссылка |
|---|---:|---|---|
| Steganography | 1/23 | Задачи на поиск скрытых данных в изображениях, файлах и метаданных | [Открыть](./steganography/) |
| Web | 15/33 | Задачи на анализ веб-приложений, HTTP, cookies, сессий и контроля доступа | [Открыть](./web/) |
| Reverse | 2/23 | Задачи на реверс-инжиниринг бинарных файлов и восстановление логики программ | [Открыть](./reverse/) |
| Misc | 0/15 | Разные задачи: нестандартная логика, кодировки, файлы и небольшие расследования | [Открыть](./misc/) |
| Cryptography | 6/20 | Задачи на шифры, кодировки, хеши и криптографические ошибки | [Открыть](./cryptography/) |
| OSINT | 1/15 | Задачи на поиск информации в открытых источниках и анализ цифровых следов | [Открыть](./osint/) |
| Forensics | 2/18 | Задачи на анализ файлов, дампов, трафика, артефактов и цифровых следов | [Открыть](./forensics/) |
| PWN | 1/10 | Задачи на эксплуатацию бинарных файлов, память и низкоуровневые уязвимости | [Открыть](./pwn/) |
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
| Журнал | OSINT | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск оригинального выпуска журнала по фрагменту обложки и нахождение программиста 39 лет | [Открыть](./osint/Magazine/) |
| Путь домой | Hardware | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Копирование значения с красного ключа-таблетки на синий через программатор KeyCopy | [Открыть](./hardware/Wayhome/) |
| Классное фото | Steganography | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Визуальная LSB-стеганография в младшем бите синего канала PNG-изображения | [Открыть](./steganography/Coolphoto/) |
| Поддержка от банка | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | IDOR в чатах поддержки: `chat_id` как MD5 от числового ID и доступ к чужому чату без подделки сессии | [Открыть](./web/Banksupport/) |
| Сломанный магазин | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Рассинхрон Telegram callback и текущей pending-заявки: покупка частей флага по цене старой дешевой заявки | [Открыть](./web/Brokenmagazine/) |
| Cookies with milk | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ cookie, base64-декодирование сессии и подмена роли пользователя для доступа к админ-панели | [Открыть](./web/Cookieswithmilk/) |
| Лысина админа | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Подделка JWT: подбор слабого HS256-secret по `rockyou.txt` и создание токена с `user=admin` | [Открыть](./web/adminsbaldhead/) |
| Умный переулок | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Старый маршрут `/api/v1/video` раскрывает ссылку на видеофайл, в кадре которого виден флаг | [Открыть](./web/SmartAlley/) |
| Студия анимаций | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | XXE в обработке SVG: чтение локальных файлов через внешнюю XML-сущность и получение флага из `/app/flag.txt` | [Открыть](./web/Animationstudio/) |
| Надежное хранилище | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Path traversal/LFI в параметре `download`: чтение PHP-исходников, SQLite-базы и подбор SHA-512 пароля `administrator` | [Открыть](./web/Securestorage/) |
| Скрытая документация | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск скрытой документации, резервного `.env` и вход в админ-панель по найденным учетным данным | [Открыть](./web/Hiddendoc/) |
| Полет нормальный | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ клиентского JavaScript, вызов `getFlag()` и XOR-расшифровка флага | [Открыть](./web/flightisnormal/) |
| Защищенный банк | Reverse | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск флага в строковых данных Windows PE-бинаря через `strings` и секцию `.rdata` | [Открыть](./reverse/SecureBank/) |
| Забытый пароль | Reverse | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ Python-скрипта с простой схемой преобразования байтов через ключ `ord()` | [Открыть](./reverse/Forgottenpassword/) |
| Логинатор | Forensics | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Извлечение флага из URL-запросов `/flag.php/<символ>` в дампе логов | [Открыть](./forensics/Loginator/) |
| NFT Маркетплейс | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | UNION SQL-инъекция в параметре `category`, чтение `sqlite_master` и извлечение флага из `s3cret.fl4g` | [Открыть](./web/NFT/) |
| Pincode | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Вход через `admin:admin` и перебор 4-значного PIN-кода с помощью Turbo Intruder | [Открыть](./web/Pincode/) |
| Предстоящий полет | PWN | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Format string bug: запись `1` в глобальную переменную `has_ticket` и переход в успешную ветку посадки | [Открыть](./pwn/Upcomingflight/) |
| Правила | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Обход проверки ознакомления и расшифровка строки из успешного `alert` через XOR с ключом `3` | [Открыть](./web/Rules/) |
| Простой API-сервер | Forensics | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск HTTP-запроса авторизации с `username=hacker` и URL-encoded флагом в pcapng-дампе | [Открыть](./forensics/simple_api/) |
| Раздача купонов | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | SQL-инъекция в параметре купона, вывод доступных купонов и применение 100% скидки | [Открыть](./web/coupons/) |
| Сила воли | Web | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Подмена JSON-параметра `clicks` в запросе покупки флага через Burp Repeater | [Открыть](./web/Willpower/) |
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
│   └── Magazine/
├── pwn/
│   └── Upcomingflight/
├── reverse/
│   ├── Forgottenpassword/
│   └── SecureBank/
├── steganography/
│   └── Coolphoto/
└── web/
    ├── adminsbaldhead/
    ├── Banksupport/
    ├── Brokenmagazine/
    ├── Cookieswithmilk/
    ├── Animationstudio/
    ├── SmartAlley/
    ├── coupons/
    ├── flightisnormal/
    ├── Hiddendoc/
    ├── NFT/
    ├── Pincode/
    ├── Rules/
    ├── Securestorage/
    ├── Willpower/
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
