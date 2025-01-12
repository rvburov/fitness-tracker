# Fitness Tracker

## Описание
`Fitness Tracker` — это приложение для анализа и отслеживания различных видов тренировок, включая бег, спортивную ходьбу и плавание. Программа рассчитывает ключевые метрики, такие как дистанция, средняя скорость и количество потраченных калорий.

## Особенности
- Поддержка трёх типов тренировок:
  - **Running** (Бег)
  - **SportsWalking** (Спортивная ходьба)
  - **Swimming** (Плавание)
- Расчёт следующих параметров для каждой тренировки:
  - Дистанция (в километрах)
  - Средняя скорость (в км/ч)
  - Потраченные калории
  - Тип тренировки
- Вывод информации о тренировке в удобном формате.

## Установка

### Требования
- Python 3.8 или выше

### Установка зависимостей
Убедитесь, что у вас установлен Python, и выполните установку зависимостей:
```bash
pip install -r requirements.txt
```

### Запуск программы
Для запуска программы выполните:
```bash
python homework.py
```

## Конфигурация

### `setup.cfg`
Конфигурация для статического анализа кода с использованием Flake8:
```ini
[flake8]
disable-noqa = True
ignore = W503
filename =
    ./homework.py
max-complexity = 10
max-line-length = 79
exclude =
  tests
```

### `pytest.ini`
Конфигурация для тестирования с использованием Pytest:
```ini
[pytest]
norecursedirs = env/*
addopts = --tb=short -rE -vv --disable-warnings -p no:cacheprovider
testpaths = tests/
python_files = test_*.py
```

## Тестирование

### Запуск тестов
Для запуска тестов выполните команду:
```bash
pytest
```

### Структура тестов
- **`tests/test_homework.py`**: Основные тесты для проверки функциональности классов и методов.
- **`tests/conftest.py`**: Конфигурация для тестов, включая утилиту для захвата вывода консоли.

## Основные файлы

### `homework.py`
Содержит реализацию основных классов:
- **`Training`**: Базовый класс для тренировок.
- **`Running`**: Класс для тренировки бега.
- **`SportsWalking`**: Класс для спортивной ходьбы.
- **`Swimming`**: Класс для плавания.

### `requirements.txt`
Список зависимостей:
```plaintext
attrs==22.1.0
flake8==5.0.4
iniconfig==1.1.1
mccabe==0.7.0
packaging==21.3
pluggy==1.0.0
py==1.11.0
pycodestyle==2.9.1
pyflakes==2.5.0
pyparsing==3.0.9
pytest==7.1.3
tomli==2.0.1
```

## Пример использования
Программа принимает входные данные в виде кодов тренировок и параметров:

```python
packages = [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180]),
]

for workout_type, data in packages:
    training = read_package(workout_type, data)
    main(training)
```

Пример вывода:
```
Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 0.994 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 336.000.
Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 481.905.
Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 349.252.
```


