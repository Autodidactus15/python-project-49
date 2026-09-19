# Brain Games

Пять математических игр в терминале на Python. Учебный проект Hexlet для практики работы с функциями, модулями и CLI-командами. Общий цикл раундов отделён от логики каждой игры.

[![Hexlet checks](https://github.com/Autodidactus15/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Autodidactus15/python-project-49/actions)

## Установка

Нужны Python `>=3.12,<4.0` и Poetry. Зависимости и команды описаны в [pyproject.toml](pyproject.toml).

```bash
git clone https://github.com/Autodidactus15/python-project-49.git
cd python-project-49
poetry install
```

## Игры

Запускайте команды из каталога проекта. Для победы нужно дать три правильных ответа подряд. Первая ошибка завершает партию; для новой партии запустите команду ещё раз. Интерфейс игр на английском.

| Команда | Задача | Формат ответа |
| --- | --- | --- |
| `poetry run brain-even` | Определить, чётное ли число | `yes` или `no` |
| `poetry run brain-calc` | Вычислить сумму, разность или произведение | Целое число |
| `poetry run brain-gcd` | Найти наибольший общий делитель двух чисел | Целое число |
| `poetry run brain-progression` | Восстановить пропущенное число арифметической прогрессии | Целое число |
| `poetry run brain-prime` | Определить, простое ли число | `yes` или `no` |

Команда `poetry run brain-games` выводит приветствие и спрашивает имя. Для запуска игры используйте одну из команд выше.

## Разработка

```bash
poetry run flake8 brain_games
poetry build
```

Первая команда проверяет стиль кода, вторая собирает пакет в `dist/`. В [Makefile](Makefile) есть эквиваленты: `make install`, `make lint` и `make build`. Для них нужен Make.

После `make build` команда `make package-install` устанавливает wheel через `python3 -m pip install dist/*.whl`. Это отдельный способ установки пакета; для игр через `poetry run` достаточно `poetry install`.

Исходники:

- [brain_games/games](brain_games/games): правила и генерация заданий для пяти игр.
- [brain_games/run_game.py](brain_games/run_game.py): общий цикл раундов и проверка ответов.
- [brain_games/scripts](brain_games/scripts): точки входа CLI-команд.

## Записи запуска

Сохранённые демонстрации в asciinema:

[Запись 1](https://asciinema.org/a/wOoi8w8qeark6j0ZmdMekuv3A) · [Запись 2](https://asciinema.org/a/rCPFYYvrcgVGHnZzpLUqu4T72) · [Запись 3](https://asciinema.org/a/tD5qroMhdeZZm7PnqPvXHSqvv) · [Запись 4](https://asciinema.org/a/KktIwfkRxQOfyn5oKRpikfDgY) · [Запись 5](https://asciinema.org/a/MbA3nuMeCutCSk5ioH8ryRxyC)
