import unittest
from animal import Animal

class Test_animal(unittest.TestCase):
    def test_animal_cat(self):
        animal1 = Animal()
        animal1.type == "cat"
        self.assertEqual(animal1.name, "Seymore")

    def test_animal_dog(self):
        animal2 = Animal()
        animal2.type == "dog"
        self.assertEqual(animal2.name, "Spot")
        
    def test_animal_name(self):
        animal1 = Animal()
        animal1.type == "cat"
        animal1.name = self.name
        animal2 = Animal()
        animal2.type == "dog"
        animal2.name = self.name

    def test_animal_size_cat(self):
        animal1 = Animal()
        animal1.type == "cat"
        animal1.size = "small"
        animal1.speak = "meow"
        animal1.size = "large"
        animal1.speak = "MEOW"

    def test_animal_size_dog(self):
        animal2 = Animal()
        animal2.type == "dog"
        animal2.size = "small"
        animal2.speak = "bow wow"
        animal2.size = "medium" 
        animal2.speak = "ruff ruff"
        animal2.size = "large"
        animal2.speak = "arf arf"

    def test_animal_age(self):
        animal1 = Animal()
        animal1.type == "cat"
        animal1.age < 10
        animal1.name + " is young"
        animal1.age >= 10
        animal1.name + " is old"

        animal2 = Animal()
        animal2.type == "dog"
        animal2.age < 10
        animal2.name + " is young"
        animal2.age >= 10
        animal2.name + " is old"