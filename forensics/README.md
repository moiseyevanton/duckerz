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
| Реинкарнация | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Восстановление удалённых файлов из ext4-образа карвингом по сигнатуре gzip и снятие матрёшки кодировок Base32→Base64→TAR→gzip | [Открыть](./Reninkation/) |
| Мим | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Перехваченный MITM-трафик (pcapng): фильтр `http`, экспорт `barabulka.jpg` через Wireshark Export Objects — флаг на картинке | [Открыть](./Mime/) |
| Сверхсекретный Шпион | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Скрытый канал в UDP-портах: `srcport−30000` = индекс, символ = `32768−dstport` — собираем флаг из заголовков | [Открыть](./TopSecretSpy/) |
| Новогодняя открытка | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | К JPEG дописан WAV-трек; флаг в спектрограмме аудио, виден только при zoom по времени (`sox trim`) | [Открыть](./NewYearscard/) |
| Офисный Хакер | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Скрытый канал в трейлере кадра (SLL trailer) под прикрытием IPP-печати; сбор флага через `tshark -e sll.trailer` | [Открыть](./OfficeHacker/) |
| Синий иней | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Bluetooth-дамп: под аудио скрыта OBEX-передача файла; тело = коды через `EF BB BF`, снимаем XOR 30 | [Открыть](./BlueFrost/) |

---

## Прогресс 📈

```text
10/18
```

---

Автор: **masquadd :)** ✍️
