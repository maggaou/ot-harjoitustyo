from datetime import datetime
from entities.user import User
from entities.move import Move

from repositories.moves_repository import moves_repository as default_moves_repository
from repositories.user_repository import user_repository as default_user_repository


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UsernameContainsCapitalLettersError(Exception):
    pass


class TooShortUsernameError(Exception):
    pass


class UsernameContainsSpacesError(Exception):
    pass


class TooShortPasswordError(Exception):
    pass


class PasswordIsNonAsciiError(Exception):
    pass


class TooShortMoveNameError(Exception):
    pass


class MoveNameIsEmptyError(Exception):
    pass


class NothingHasChangedError(Exception):
    pass


class MovesService:
    """Sovelluslogiikka."""

    def __init__(
            self,
            moves_repository=default_moves_repository,
            user_repository=default_user_repository
    ):
        """Luokan konstruktori.

        Args:
            moves_repository: 
                Oletus MovesRepository-olio.
            user_repository:
                Oletus UserRepository-olio.
        """

        self._user = None
        self._moves_repository = moves_repository
        self._user_repository = user_repository

    def create_move(self, **args):
        """Uuden liikkeen luonti.

        Args:
            **args: liikkeen sisältö (content) ja mahdollinen metadata.
        Raises:
            MoveNameIsEmpty:
                Lähettää virheen jos liikkeelle ei ole annettu nimeä.
        Returns:
            Luotu liike (Move-olio).
        """
        if "name" not in args or not args["name"]:
            raise MoveNameIsEmptyError("Name must be not empty")

        args_clean = self._clean_args(args)

        if len(args_clean["name"]) < 5:
            raise TooShortMoveNameError(
                "Move name must be five characters or more")

        args_clean["original_creator"] = self._user.username
        move = Move(**args_clean)
        return self._moves_repository.create(move)

    def return_all(self):
        """Palauttaa kaikki liikkeet.

        Returns:
            Palauttaa kaikki ohjelmaan tallennetut liikkeet.
        """
        return self._moves_repository.find_all()

    def login(self, username, password):
        """Sisäänkirjautuminen.

        Args:
            username: käyttäjänimi.
            password: salasana.
        Returns:
            Kirjautunut käyttäjä (User-olio).
        Raises:
            InvalidCredentialsError:
                Ohjelma lähettää virheen jos käyttäjänimi ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_logged_in_user(self):
        """Palauttaa tällä hetkellä kirjautuneen käyttäjän.

        Returns:
            Kirjautunut käyttäjä (User-olio).
        """
        return self._user

    def get_all_users(self):
        """Palauttaa kaikki ohjelmaan tallennetut käyttäjät.

        Returns:
            Lista (User-oliot).
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None

    def create_new_user(self, username, password):
        """Luo uuden käyttäjän ja kirjaa tämän sisään.

        Args:
            username: käyttäjätunnus.
            password: salasana.
        Raises:
            UsernameExistsError:
                Ohjelma lähettää virheen jos käyttäjätunnus on jo käytössä.
            UsernameContainsSpacesError:
                Lähetä virhe jos username sisältää välilyöntejä.
            TooShortUsernameError:
                Lähetä virhe jos username on liian lyhyt.
            UsernameContainsCapitalLettersError:
                Salli ainoastaan pienet kirjaimet käyttäjänimessä.
            TooShortPasswordError:
                Salli ainoastaan salasana jonka pituus on vähintään 8 merkkiä.
            PasswordIsNonAsciiError:
                Salli ainoastaan salasana joka sisältää ASCII merkkejä.
        Returns:
            Palauttaa luodun käyttäjän (User-olio).
        """
        if ' ' in username:
            raise UsernameContainsSpacesError

        if len(username) < 3:
            raise TooShortUsernameError

        if any(c.isupper() for c in username):
            raise UsernameContainsCapitalLettersError

        if len(password) < 8:
            raise TooShortPasswordError

        if not password.isascii():
            raise PasswordIsNonAsciiError

        hi = self._user_repository.find_by_username(username)

        if hi:
            raise UsernameExistsError(
                f"Username {username} is already created")

        user = User(username=username, password=password)

        self._user = user

        return self._user_repository.create(user)

    def delete_move(self, move):
        """Poistaa annetun liikkeen.

        Args:
            move: poistettava move-olio.
        """
        self._moves_repository.delete(move)

    def find_by_uid(self, uid):
        """Etsi liike tunnisteen perusteella.

        Args:
            uid: liikkeen tunniste.
        Returns:
            move-objekti.
        """
        return self._moves_repository.find_by_uid(uid)

    def edit_move(self, **args):
        """Tallentaa muokatun version annetusta liikkeestä.

        Args:
            **args: liikkeen sisältö (content) ja mahdollinen metadata.
        """
        editable_fields = [
            "name",
            "content",
            "style",
            "age_group",
            "difficulty",
            "picture_link",
            "reference",
        ]

        if "name" not in args or not args["name"]:
            raise MoveNameIsEmptyError("Name must be not empty")

        args_clean = self._clean_args(args)

        if len(args_clean["name"]) < 5:
            raise TooShortMoveNameError(
                "Move name must be five characters or more")

        move_old = self._moves_repository.find_by_uid(args_clean["uid"])
        move_old_args = dict(vars(move_old))

        i_have_seen_changes = False
        for field in editable_fields:
            if args_clean[field] != move_old_args[field]:
                i_have_seen_changes = True

        if not i_have_seen_changes:
            raise NothingHasChangedError("Nothing has changed")

        current_date_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        args_clean["modifications"].append(
            (current_date_str, moves_service.get_logged_in_user().username))

        move = Move(**args_clean)
        self._moves_repository.modify(move)

    @staticmethod
    def _clean_args(args):
        args_copy = dict(args)
        for field in args:
            if args[field] and isinstance(args[field], str):
                args_copy[field] = args[field].strip()

        return args_copy


moves_service = MovesService()
