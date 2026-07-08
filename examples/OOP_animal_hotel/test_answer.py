"""Tests for the animal_food example."""

import unittest
import answer

class TestAnimalFood(unittest.TestCase):
    def test_young_dog_needs_more_food(self):
        dog = answer.Dog("Bello", 3)
        self.assertEqual(dog.get_food(), 0.4)

    def test_old_dog_needs_less_food(self):
        dog = answer.Dog("Rex", 7)
        self.assertEqual(dog.get_food(), 0.3)

    def test_young_cat_needs_less_food(self):
        cat = answer.Cat("Mimi", 0.5)
        self.assertEqual(cat.get_food(), 0.2)

    def test_old_cat_needs_normal_food(self):
        cat = answer.Cat("Luna", 2)
        self.assertEqual(cat.get_food(), 0.3)

    def test_cat_uses_description_from_animal(self):
        cat = answer.Cat("Mimi", 0.5)
        self.assertEqual(cat.describe(), "Mimi is 0.5 years old.")

    def test_calculate_total_food_for_mixed_animals(self):
        animals = [
            answer.Dog("Bello", 3),
            answer.Dog("Rex", 7),
            answer.Cat("Mimi", 0.5),
            answer.Cat("Luna", 2),
        ]
        self.assertEqual(answer.calculate_total_food(animals), 1.2)
