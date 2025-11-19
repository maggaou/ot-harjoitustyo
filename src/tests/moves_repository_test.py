from pathlib import Path
import unittest
from entities.age_group import AgeGroup
from entities.difficulty import Difficulty
from entities.move import Move
from entities.style import Style
from repositories.moves_repository import MOVES_REPOSITORY


class TestMovesRepository(unittest.TestCase):
    def setUp(self):
        self.moves_repository = MOVES_REPOSITORY
        self.moves_repository.delete_all()

        self.m1 = Move(content="jeihou")
        self.m2 = Move(content="jööpöö")

    def test_wrestling_style_as_string(self):
        self.assertEqual(Style.GR, "Greco-Roman")

    def test_age_group_as_string(self):
        self.assertEqual(AgeGroup.SIX, "6 years old and above")

    def test_difficulty_as_string(self):
        self.assertEqual(Difficulty.BASIC, "basic")

    def test_write_move_works(self):
        self.moves_repository.create(self.m1)
        moves = self.moves_repository.find_all()
        hi = moves.pop()

        self.assertEqual(hi.content, self.m1.content)

    def test_creating_and_storing_multiple_moves1(self):
        self.moves_repository.create(self.m1)
        self.moves_repository.create(self.m2)

        path = Path(self.moves_repository.directory)
        files = list(path.glob("*.md"))
        self.assertEqual(len(files), 2)

        moves = self.moves_repository.find_all()
        self.assertEqual(len(moves), 2)

    def test_move_ids_are_unique(self):
        id1 = self.m1.uid
        id2 = self.m2.uid
        self.assertFalse(id1 == id2)

    def test_creating_and_storing_multiple_moves2(self):
        self.moves_repository.create(self.m1)
        self.moves_repository.create(self.m2)

        moves = self.moves_repository.find_all()

        self.assertTrue(self.m1 in moves)
        self.assertTrue(self.m2 in moves)
