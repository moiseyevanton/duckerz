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
| Cookies with milk | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Cookie tampering: base64-декодирование сессии и подмена `status` на `admin` | [Открыть](./Cookieswithmilk/) |
| Лысина админа | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Подделка JWT: подбор слабого HS256-secret по `rockyou.txt` и создание токена с `user=admin` | [Открыть](./adminsbaldhead/) |
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
10/33
```

---

Автор: **masquadd :)** ✍️
