from pathlib import Path
import unittest
from entities.move import Move
from repositories.moves_repository import moves_repository


class TestMovesRepository(unittest.TestCase):
    def setUp(self):
        self.moves_repository = moves_repository
        self.moves_repository.delete_all()

        self.m1 = Move(content="jeihou")
        self.m2 = Move(content="jööpöö")

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

    def test_delete_all(self):
        self.moves_repository.create(self.m1)
        self.moves_repository.create(self.m2)

        self.moves_repository.delete_all()
        hi = self.moves_repository.find_all()

        self.assertFalse(hi)

    def test_deleting_one_move(self):
        self.moves_repository.create(self.m1)
        self.moves_repository.create(self.m2)

        self.moves_repository.delete(self.m2)

        moves = self.moves_repository.find_all()
        self.assertFalse(self.m2 in moves)

    def test_modify_move_content(self):
        self.moves_repository.create(self.m1)
        old_content = self.m1.content

        self.m1.content = "my new content"
        self.moves_repository.modify(self.m1)

        hi = self.moves_repository.find_all().pop()
        self.assertNotEqual(hi.content, old_content)
        self.assertEqual(hi.content, "my new content")

    def test_modify_move_name(self):
        self.moves_repository.create(self.m1)
        old_name = self.m1.name

        self.m1.name = "nice move"
        self.moves_repository.modify(self.m1)

        hi = self.moves_repository.find_all().pop()
        self.assertNotEqual(hi.name, old_name)
        self.assertEqual(hi.name, "nice move")

    def test_find_by_uid(self):
        self.m1.name = "my nice move"
        self.moves_repository.create(self.m1)
        hi = self.moves_repository.find_by_uid(self.m1.uid)

        self.assertEqual(hi.uid, self.m1.uid)
        self.assertEqual(hi.name, "my nice move")
        self.assertEqual(hi.content, "jeihou")

    def test_move_modifications_are_lists(self):
        self.assertTrue(isinstance(self.m1.modifications, list))
        self.m1.modifications.append(('a', 'b'))
        self.m1.modifications.append(('b', 'c'))

        self.moves_repository.create(self.m1)
        hi = self.moves_repository.find_all().pop()

        self.assertTrue(isinstance(hi.modifications, list))

        hi = self.moves_repository.find_by_uid(self.m1.uid)
        self.assertTrue(isinstance(hi.modifications, list))
