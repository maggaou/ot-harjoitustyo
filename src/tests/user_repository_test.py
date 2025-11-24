import unittest
from repositories.user_repository import user_repository
from entities.user import User
from initialize_database import initialize_database


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = user_repository
        self.user_repository.delete_all()
        self.u1 = User(name="Roope Koivisto", team="Nurmon Voima",
                       username="roopeKoi", password="password1@")
        self.u2 = User(name="Jenni Järvinen", team="Lappajärven Veikot",
                       username="jenni1", password="-salasana-")

    def test_create(self):
        self.user_repository.create(self.u1)
        users = self.user_repository.find_all()

        self.assertEqual(len(users), 1)

    def test_username_is_created_and_stored_correctly(self):
        self.user_repository.create(self.u1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.username, self.u1.username)

    def test_name_is_created_and_stored_correctly(self):
        self.user_repository.create(self.u1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.name, self.u1.name)

    def test_team_is_created_and_stored_correctly(self):
        self.user_repository.create(self.u1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.team, self.u1.team)

    def test_password_is_created_and_stored_correctly(self):
        self.user_repository.create(self.u1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.password, self.u1.password)

    def test_creating_and_storing_multiple_users(self):
        self.user_repository.create(self.u1)
        self.user_repository.create(self.u2)
        users = self.user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0], self.u1)
        self.assertEqual(users[1], self.u2)

    def test_find_by_username_returns_user_if_found(self):
        self.user_repository.create(self.u1)

        u = self.user_repository.find_by_username(self.u1.username)

        self.assertEqual(u, self.u1)

    def test_find_by_username_returns_none_if_not_found(self):
        self.user_repository.create(self.u1)

        u = self.user_repository.find_by_username("jeihou")

        self.assertEqual(u, None)

    def test_find_all_returns_empty_list_after_delete_all(self):
        self.user_repository.create(self.u1)
        self.user_repository.create(self.u2)

        self.user_repository.delete_all()

        hi = self.user_repository.find_all()
        self.assertEqual(type(hi), list)
        self.assertEqual(len(hi), 0)
