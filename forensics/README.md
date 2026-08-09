# Forensics 🕵️

Раздел с writeup-отчетами по forensics-задачам платформы [Duckerz](https://duckerz.ru/).

В этой категории обычно встречаются:
- анализ файлов и их структуры;
- исследование дампов памяти;
- анализ сетевого трафика;
- восстановление удаленных или скрытых данных;
- поиск артефактов в системных следах.

---

## Решенные задачи ✅

| Задача | Сложность | Описание | Ссылка |
|---|---|---|---|
| Логинатор | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Извлечение флага из URL-запросов `/flag.php/<символ>` в дампе логов | [Открыть](./Loginator/) |
| Простой API-сервер | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск HTTP-запроса авторизации с `username=hacker` и URL-encoded флагом в pcapng-дампе | [Открыть](./simple_api/) |
| Ищейка | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск флага в открытом виде в дампе RAM VMware (`.vmem`) через `strings` + `grep PolyCTF` | [Открыть](./Bloodhound/) |
| Менеджер | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Разбор журнала событий Windows (`.evtx`) через `python-evtx`: событие Ntfs 98 связывает `HarddiskVolume4` с `DriveName` (GUID тома) | [Открыть](./Manager/) |

---

## Прогресс 📈

```text
4/18
```

---

Автор: **masquadd :)** ✍️
