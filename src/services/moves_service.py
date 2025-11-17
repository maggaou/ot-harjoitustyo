from entities.user import User
from entities.move import Move

from repositories.moves_repository import MOVES_REPOSITORY as default_moves_repository
from repositories.user_repository import USER_REPOSITORY as default_user_repository

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
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
        Returns:
            Luotu liike (Move-olio).
        """
        args["original_creator"] = self._user.username

        move = Move(**args)
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

    def create_new_user(self, username, password, name=None, team=None):
        """Luo uuden käyttäjän ja kirjaa tämän sisään.

        Args:
            username: käyttäjätunnus.
            password: salasana.
            name: valmentajan nimi.
            team: valmentajan seura.
        Raises:
            UsernameExistsError:
                Ohjelma lähettää virheen jos käyttäjätunnus on jo käytössä.
        Returns:
            Palauttaa luodun käyttäjän (User-olio).
        """

        hi = self._user_repository.find_by_username(username)

        if hi:
            raise UsernameExistsError(f"Username {username} is already created")

        user = User(name=name,team=team,username=username, password=password)

        self._user = user

        return self._user_repository.create(user)

MOVES_SERVICE = MovesService()
