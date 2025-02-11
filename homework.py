from dataclasses import dataclass, asdict
from typing import Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        message_template = 'Тип тренировки: {training_type}; ' \
                           'Длительность: {duration:.3f} ч.; ' \
                           'Дистанция: {distance:.3f} км; ' \
                           'Ср. скорость: {speed:.3f} км/ч; ' \
                           'Потрачено ккал: {calories:.3f}.'
        return message_template.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_H: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""
    CCALORIES_MEAN_SPEED_MULTIPLIER_RUN: int = 18
    CCALORIES_MEAN_SPEED_SHIFT_RUN: float = 1.79

    def get_spent_calories(self) -> float:
        return ((self.CCALORIES_MEAN_SPEED_MULTIPLIER_RUN
                * self.get_mean_speed()
                + self.CCALORIES_MEAN_SPEED_SHIFT_RUN) * self.weight
                / self.M_IN_KM
                * self.duration * self.MIN_IN_H)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CCALORIES_MEAN_SPEED_MULTIPLIER_WALK: float = 0.035
    CCALORIES_MEAN_SPEED_SHIFT_WALK: float = 0.029
    KMH_IN_MSEC: float = 0.278
    CM_IN_M: int = 100

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.CCALORIES_MEAN_SPEED_MULTIPLIER_WALK * self.weight
                + (self.get_mean_speed() * self.KMH_IN_MSEC)
                ** 2 / (self.height / self.CM_IN_M)
                * self.CCALORIES_MEAN_SPEED_SHIFT_WALK * self.weight)
                * (self.duration * self.MIN_IN_H))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CCALORIES_MEAN_SPEED_MULTIPLIER_SWIMMING: float = 1.1
    CCALORIES_MEAN_SPEED_SHIFT_SWIMMING: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool
                * self.count_pool
                / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed()
                + self.CCALORIES_MEAN_SPEED_MULTIPLIER_SWIMMING)
                * self.CCALORIES_MEAN_SPEED_SHIFT_SWIMMING
                * self.weight
                * self.duration)


WORKOUT: Dict[str, Type[Training]] = {'SWM': Swimming,
                                      'RUN': Running,
                                      'WLK': SportsWalking}


def read_package(workout_type: str, data: list[float]) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type not in WORKOUT:
        raise ValueError("Несуществующий код тренировки")
    return WORKOUT[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
