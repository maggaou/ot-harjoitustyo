import unittest
from entities.style import Style

class TestMovesRepository(unittest.TestCase):
    def test_wrestling_style_as_string(self):
        self.assertEqual(Style.GR, "Greco-Roman")

