import unittest
from entities.age_group import AgeGroup
from entities.difficulty import Difficulty
from entities.style import Style

class TestMovesRepository(unittest.TestCase):
    def test_wrestling_style_as_string(self):
        self.assertEqual(Style.GR, "Greco-Roman")

    def test_age_group_as_string(self):
        self.assertEqual(AgeGroup.SIX, "6 years old and above")
    
    def test_difficulty_as_string(self):
        self.assertEqual(Difficulty.BASIC, "basic")