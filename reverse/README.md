# Reverse 🔁

Раздел с writeup-отчетами по reverse engineering на платформе [Duckerz](https://duckerz.ru/).

В этой категории обычно встречаются:
- анализ бинарных файлов;
- восстановление логики программы;
- поиск проверок флага;
- дизассемблирование и отладка;
- анализ строк, функций и условий.

---

## Решенные задачи ✅

| Задача | Сложность | Описание | Ссылка |
|---|---|---|---|
| Защищенный банк | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Поиск флага в строковых данных Windows PE-бинаря через `strings` и секцию `.rdata` | [Открыть](./SecureBank/) |
| Забытый пароль | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Анализ Python-скрипта с простой схемой преобразования байтов через ключ `ord()` | [Открыть](./Forgottenpassword/) |
| Матрёшка | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | Многослойный шифр в `.pyc`: декомпиляция байткода и обращение цепочки binary/atbash/reverse/rot13-сдвиг/XOR | [Открыть](./Matryoshka/) |
| Очень защищённый банк | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | PE32+ x86-64: SHA-256-проверка пина в Ghidra, обход через патч `jne`→`nop` в radare2 и запуск под wine | [Открыть](./Ahighlysecurebank/) |
| ПлюсМинус | ![Easy](https://img.shields.io/badge/Easy-Green?style=for-the-badge) | ELF x86-64 (not stripped): `decrypt_flag` вычитает 10 из байтов `encrypted_flag` — обращаем сдвиг Цезаря | [Открыть](./PlusMinus/) |

---

## Прогресс 📈

```text
5/23
```

---

Автор: **masquadd :)** ✍️
