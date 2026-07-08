"""Reference solution for the animal_food example."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Base class for all animals in the pet hotel."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        """Return a short description of the animal."""
        return f"{self.name} is {self.age} years old."

    @abstractmethod
    def get_food(self) -> float:
        """Return the food amount needed in kilograms."""
        pass


class Dog(Animal):
    """A dog in the pet hotel."""
    def get_food(self):
        """Return the food amount needed for this dog."""
        if self.age < 5:
            return 0.4
        return 0.3


class Cat(Animal):
    """A cat in the pet hotel."""
    def get_food(self):
        """Return the food amount needed for this cat."""
        if self.age < 1:
            return 0.2
        return 0.3


def calculate_total_food(animals):
    """Return the total food amount needed for all animals."""
    total_food = 0

    for animal in animals:
        total_food += animal.get_food()

    return total_food