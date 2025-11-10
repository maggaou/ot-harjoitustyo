import unittest
from entities.user import User
from entities.move import Move
from services.moves_service import (
    MoveService, 
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
        self.moves_service = MoveService(FakeMovesRepository(), FakeUserRepository())

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
