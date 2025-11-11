import unittest
from entities.user import User
from entities.move import Move
from services.moves_service import (
    MovesService, 
    InvalidCredentialsError, 
    UsernameExistsError
)

class FakeMovesRepository:
    def __init__(self, moves=None):
        self.moves = moves or []

    def find_all(self):
        return self.moves
    
    def create(self, move):
        self.moves.append(move)

        return move
    
    def delete_all(self):
        self.moves = []

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users
    
    def find_by_username(self, username):
        hello = [u for u in self.users if u.username == username]
    
        if len(hello) > 0:
            return hello[0]
        else:
            return None
    
    def create(self, user):
        self.users.append(user)

        return user
    
    def delete_all(self):
        self.users = []

class TestMovesService(unittest.TestCase):
    def setUp(self):
        self.moves_service = MovesService(FakeMovesRepository(), FakeUserRepository())

        self.m1 = Move(content="mörkö")
        self.m2 = Move(content="pöö")
        self.u1 = User(username="User1", password="1234")

    def login_user(self, user):
        self.moves_service.create_new_user(user.username, user.password)

    def test_creating_moves_has_correct_creator(self):
        self.login_user(self.u1)

        args = {"content": "my content"}
        self.moves_service.create_move(**args)

        moves = self.moves_service.return_all()

        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0].original_creator, self.u1.username)

    def test_creating_moves_has_correct_content(self):
        self.login_user(self.u1)
        
        args = {"content": "my content"}
        self.moves_service.create_move(**args)

        moves = self.moves_service.return_all()

        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0].content, "my content")
    
    def test_get_logged_in_user(self):
        self.login_user(self.u1)

        hello = self.moves_service.get_logged_in_user()

        self.assertEqual(hello, self.u1)

    def test_create_new_user_with_non_existing_username(self):
        username = self.u1.username
        password = self.u1.password

        self.moves_service.create_new_user(username, password)

        users = self.moves_service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_new_user_with_existing_username(self):
        username = self.u1.username

        self.moves_service.create_new_user(username, "1234")

        self.assertRaises(UsernameExistsError, self.moves_service.create_new_user, username, '')

    def test_login_with_valid_username_and_password(self):
        self.moves_service.create_new_user(self.u1.username, self.u1.password)

        u = self.moves_service.login(self.u1.username, self.u1.password)

        self.assertEqual(u, self.u1)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(InvalidCredentialsError, self.moves_service.login, 'jeihoo', '')

    def test_logout_sets_active_user_to_none(self):
        self.login_user(self.u1)
        self.moves_service.logout()
        self.assertIsNone(self.moves_service.get_logged_in_user())