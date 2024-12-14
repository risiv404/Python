from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Класс, описывающий животное.

    Атрибуты:
        name (str): имя животного.
        age (int): возраст животного в годах.

    Методы:
        speak(): воспроизводит звук животного.
        is_adult(): проверяет, является ли животное взрослым.
    """

    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self) -> str:
        """
        Издает звук, характерный для животного.

        :return: строка с описанием звука животного.

        >>> dog = Dog("Рекс", 3)
        >>> dog.speak()
        'Гав'
        """
        ...

    @abstractmethod
    def is_adult(self) -> bool:
        """
        Проверяет, является ли животное взрослым.

        :return: True, если животное взрослое, иначе False.

        >>> dog = Dog("Рекс", 3)
        >>> dog.is_adult()
        True
        """
        ...


class Dog(Animal):
    """
    Класс, описывающий собаку, наследуется от Animal.

    Атрибуты:
        name (str): имя собаки.
        age (int): возраст собаки в годах.

    Методы:
        speak(): воспроизводит звук собаки.
        is_adult(): проверяет, является ли собака взрослой.
    """

    def speak(self) -> str:
        """Издает звук собаки."""
        return "Гав"

    def is_adult(self) -> bool:
        """Проверяет, является ли собака взрослой (возраст 1 года и более)."""
        return self.age >= 1


class Bird(Animal):
    """
    Класс, описывающий птицу, наследуется от Animal.

    Атрибуты:
        name (str): имя птицы.
        age (int): возраст птицы в годах.

    Методы:
        speak(): воспроизводит звук птицы.
        is_adult(): проверяет, является ли птица взрослой.
    """

    def speak(self) -> str:
        """Издает звук птицы."""
        return "Чирик"

    def is_adult(self) -> bool:
        """Проверяет, является ли птица взрослой (возраст 1 года и более)."""
        return self.age >= 1


if __name__ == "__main__":
    # Пример использования doctest для проверки методов
    import doctest

    doctest.testmod()
