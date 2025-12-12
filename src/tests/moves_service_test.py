import unittest
from entities.user import User
from entities.move import Move
from services.moves_service import (
    MovesService,
    InvalidCredentialsError,
    NothingHasChangedError,
    UsernameExistsError,
    MoveNameIsEmptyError,
    TooShortMoveNameError,
    UsernameContainsCapitalLettersError,
    TooShortUsernameError,
    UsernameContainsSpacesError,
    TooShortPasswordError,
    PasswordIsNonAsciiError,
)


class FakeMovesRepository:
    def __init__(self, moves=None):
        self.moves = moves or []

    def find_all(self):
        return self.moves

    def find_by_uid(self, uid):
        for move in self.moves:
            if move.uid == uid:
                return move
        return None

    def create(self, move):
        self.moves.append(move)

        return move

    def delete_all(self):
        self.moves = []

    def modify(self, move):
        index = self.moves.index(move)
        self.moves[index] = move


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
        self.moves_service = MovesService(
            FakeMovesRepository(), FakeUserRepository())

        self.m1 = Move(content="mörkö")
        self.m2 = Move(content="pöö")
        self.u1 = User(username="user1", password="12345678")

    def login_user(self, user):
        self.moves_service.create_new_user(user.username, user.password)

    def test_creating_moves_has_correct_creator(self):
        self.login_user(self.u1)

        args = {"name": "m1 m1 m1",
                "content": "my content"}
        self.moves_service.create_move(**args)

        moves = self.moves_service.return_all()

        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0].original_creator, self.u1.username)

    def test_creating_moves_has_correct_content(self):
        self.login_user(self.u1)

        args = {"name": "m1 m1 m1",
                "content": "my content"}
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

        self.moves_service.create_new_user(username, self.u1.password)

        self.assertRaises(UsernameExistsError,
                          self.moves_service.create_new_user, username, '12345678')

    def test_create_new_user_with_capital_letters(self):
        self.assertRaises(UsernameContainsCapitalLettersError,
                          self.moves_service.create_new_user, "User1", '')
        self.assertRaises(UsernameContainsCapitalLettersError,
                          self.moves_service.create_new_user, "useR1", '')
        self.assertRaises(UsernameContainsCapitalLettersError,
                          self.moves_service.create_new_user, "USER", '')

    def test_create_new_user_with_short_username(self):
        self.assertRaises(TooShortUsernameError,
                          self.moves_service.create_new_user, "aa", '')
        self.assertRaises(TooShortUsernameError,
                          self.moves_service.create_new_user, "a", '')

    def test_create_new_user_with_spaces(self):
        self.assertRaises(UsernameContainsSpacesError,
                          self.moves_service.create_new_user, "aaaa ", '')
        self.assertRaises(UsernameContainsSpacesError,
                          self.moves_service.create_new_user, " aaaa", '')
        self.assertRaises(UsernameContainsSpacesError,
                          self.moves_service.create_new_user, "a aaa", '')

    def test_create_new_user_with_short_password(self):
        self.assertRaises(TooShortPasswordError,
                          self.moves_service.create_new_user, "me_user", "1234567")

    def test_create_new_user_with_non_ascii_password(self):
        self.assertRaises(PasswordIsNonAsciiError,
                          self.moves_service.create_new_user, "my_user", "öööööööööö")
        self.assertRaises(PasswordIsNonAsciiError,
                          self.moves_service.create_new_user, "my_user", "1234567å")
        self.assertRaises(PasswordIsNonAsciiError,
                          self.moves_service.create_new_user, "my_user", "1234567ä")
        self.assertRaises(PasswordIsNonAsciiError,
                          self.moves_service.create_new_user, "my_user", "привет123")

    def test_create_new_user_with_3letters_is_allowed(self):
        user = self.moves_service.create_new_user("moi", "12345678")
        self.assertIsInstance(user, User)
        self.assertTrue(user.username, "moi")
        self.assertTrue(user.password, "12345678")

    def test_login_with_valid_username_and_password(self):
        self.moves_service.create_new_user(self.u1.username, self.u1.password)

        u = self.moves_service.login(self.u1.username, self.u1.password)

        self.assertEqual(u, self.u1)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(InvalidCredentialsError,
                          self.moves_service.login, 'jeihoo', '')

    def test_logout_sets_active_user_to_none(self):
        self.login_user(self.u1)
        self.moves_service.logout()
        self.assertIsNone(self.moves_service.get_logged_in_user())

    def test_create_empty_move(self):
        args1 = {}
        args2 = {"name": ""}
        args3 = {"name": None}
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.create_move, **args1)
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.create_move, **args2)
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.create_move, **args3)

    def test_edit_move_with_empty_name(self):
        args1 = {}
        args2 = {"name": ""}
        args3 = {"name": None}
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.edit_move, **args1)
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.edit_move, **args2)
        self.assertRaises(MoveNameIsEmptyError,
                          self.moves_service.edit_move, **args3)

    def test_edit_move_with_no_changes(self):
        self.login_user(self.u1)
        args = {
            "name": "my nice move 1",
            "content": "my content"
        }
        move = self.moves_service.create_move(**args)
        args.update(vars(move))
        self.assertRaises(NothingHasChangedError,
                          self.moves_service.edit_move, **args)

    def test_edit_move_with_short_name(self):
        self.login_user(self.u1)
        args = {
            "name": "my nice move 1",
            "content": "content",
        }
        move = self.moves_service.create_move(**args)
        args.update(vars(move))
        args.update({
            "name": "1234"
        })
        self.assertRaises(TooShortMoveNameError,
                          self.moves_service.edit_move, **args)

    def test_create_move_with_short_name(self):
        self.login_user(self.u1)
        args = {
            "name": "1234",
        }
        self.assertRaises(TooShortMoveNameError,
                          self.moves_service.create_move, **args)

    def test_create_move_with_extra_whitespace1(self):
        self.login_user(self.u1)
        args1 = {
            "name": "          "
        }
        args2 = {
            "name": "  moi"
        }
        args3 = {
            "name": "moi  "
        }
        self.assertRaises(TooShortMoveNameError,
                          self.moves_service.create_move, **args1)
        self.assertRaises(TooShortMoveNameError,
                          self.moves_service.create_move, **args2)
        self.assertRaises(TooShortMoveNameError,
                          self.moves_service.create_move, **args3)

    def test_create_move_with_extra_whitespace2(self):
        self.login_user(self.u1)
        args1 = {
            "name": "    aaaaa      "
        }
        args2 = {
            "name": "  bbbbb"
        }
        args3 = {
            "name": "ccccc  "
        }
        self.moves_service.create_move(**args1)
        self.moves_service.create_move(**args2)
        self.moves_service.create_move(**args3)

        moves = self.moves_service.return_all()
        move_names = [move.name for move in moves]

        self.assertTrue("aaaaa" in move_names)
        self.assertTrue("bbbbb" in move_names)
        self.assertTrue("ccccc" in move_names)

