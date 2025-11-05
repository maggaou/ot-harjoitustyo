import unittest
from repositories.user_repository import USER_REPOSITORY
from entities.user import User
from initialize_database import initialize_database


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_repository = USER_REPOSITORY
        self.user_repository.delete_all()
        self.user_test1 = User(name="Roope Koivisto", team="Nurmon Voima",
                               username="roopeKoi", password="password1@")
        self.user_test2 = User(name="Jenni Järvinen", team="Lappajärven Veikot",
                               username="jenni1", password="-salasana-")

    def test_create(self):
        self.user_repository.create(self.user_test1)
        users = self.user_repository.find_all()

        self.assertEqual(len(users),1)

    def test_username_is_created_and_stored_correctly(self):
        self.user_repository.create(self.user_test1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.username, self.user_test1.username)

    def test_name_is_created_and_stored_correctly(self):
        self.user_repository.create(self.user_test1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.name, self.user_test1.name)

    def test_team_is_created_and_stored_correctly(self):
        self.user_repository.create(self.user_test1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.team, self.user_test1.team)

    def test_password_is_created_and_stored_correctly(self):
        self.user_repository.create(self.user_test1)
        users = self.user_repository.find_all()

        u = users.pop()
        self.assertEqual(u.password, self.user_test1.password)