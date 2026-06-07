# Web 🌐

Раздел с writeup-отчетами по веб-задачам платформы [Duckerz](https://duckerz.ru/).

В этой категории обычно встречаются:
- анализ HTTP-запросов и ответов;
- работа с cookies и сессиями;
- ошибки авторизации и контроля доступа;
- уязвимости в логике приложения;
- инъекции, обходы фильтров и работа с параметрами.

---

## Решенные задачи ✅

| Задача | Сложность | Описание | Ссылка |
|---|---|---|---|
| Поддержка от банка | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | IDOR в чатах поддержки: `chat_id` как MD5 от числового ID и доступ к чужому чату без подделки сессии | [Открыть](./Banksupport/) |
| Сломанный магазин | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Рассинхрон Telegram callback и текущей pending-заявки: покупка частей флага по цене старой дешевой заявки | [Открыть](./Brokenmagazine/) |
| Cookies with milk | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Cookie tampering: base64-декодирование сессии и подмена `status` на `admin` | [Открыть](./Cookieswithmilk/) |
| Лысина админа | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Подделка JWT: подбор слабого HS256-secret по `rockyou.txt` и создание токена с `user=admin` | [Открыть](./adminsbaldhead/) |
| Начинающий жонглер | ![Medium](https://img.shields.io/badge/Medium-Orange?style=for-the-badge) | Magic hash в PHP: обход проверки `md5($code) == "0e..."` через строку с MD5 вида `0e<digits>` | [Открыть](./Aspiringjuggler/) |
| Редактор тем | ![Medium](https://img.shields.io/badge/Medium-Orange?style=for-the-badge) | XSS через `#theme=`: обход валидации в `window.onload`, инъекция через `innerHTML` и кража cookie админа через webhook | [Открыть](./Themeeditor/) |
| Умный переулок | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Старый маршрут `/api/v1/video` раскрывает ссылку на видеофайл, в кадре которого виден флаг | [Открыть](./SmartAlley/) |
| Студия анимаций | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | XXE в обработке SVG: чтение локальных файлов через внешнюю XML-сущность и получение флага из `/app/flag.txt` | [Открыть](./Animationstudio/) |
| Надежное хранилище | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Path traversal/LFI в параметре `download`: чтение PHP-исходников, SQLite-базы и подбор SHA-512 пароля `administrator` | [Открыть](./Securestorage/) |
| Скрытая документация | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск скрытой документации, резервного `.env` и вход в админ-панель по найденным учетным данным | [Открыть](./Hiddendoc/) |
| Полет нормальный | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ клиентского JavaScript, вызов `getFlag()` и XOR-расшифровка флага | [Открыть](./flightisnormal/) |
| Pincode | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Вход через `admin:admin` и перебор 4-значного PIN-кода с помощью Turbo Intruder | [Открыть](./Pincode/) |
| NFT Маркетплейс | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | UNION SQL-инъекция в параметре `category`, чтение `sqlite_master` и извлечение флага из `s3cret.fl4g` | [Открыть](./NFT/) |
| Правила | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Обход проверки ознакомления и расшифровка строки из успешного `alert` через XOR с ключом `3` | [Открыть](./Rules/) |
| Раздача купонов | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | SQL-инъекция в параметре купона, вывод доступных купонов и применение 100% скидки | [Открыть](./coupons/) |
| Сила воли | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Подмена JSON-параметра `clicks` в запросе покупки флага через Burp Repeater | [Открыть](./Willpower/) |
| Web polygon | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Получение частей флага через разные HTTP-методы и GET-параметр на `/flag` | [Открыть](./webpolygon/) |

---

## Задачи в работе 🧪

Пока пусто.

---

## Прогресс 📈

```text
17/33
```

---

Автор: **masquadd :)** ✍️
