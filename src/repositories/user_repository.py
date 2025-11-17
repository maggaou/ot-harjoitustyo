

from database_connection import get_database_connection
from entities.user import User


class UserRepository():

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: tietokantayhteyden Connection-objekti
        """
        self._connection = connection

    def delete_all(self):
        """Tyhjentää Users-taulun
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from Users")

        self._connection.commit()

    def create(self, user):
        """Käyttäjän tallennus (Users-taulun schema)

        Args:
            user: tallennettava käyttäjä (User olio)

        Returns:
            Tallennettu käyttäjä (User olio)
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Users (name, team, username, password) VALUES (?, ?, ?, ?)",
            (user.name, user.team, user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_all(self):
        """Palauttaa kaikki valmentajat

        Returns:
            Lista (User-oliot)
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")

        rows = cursor.fetchall()

        users = []
        for row in rows:
            u = create_user_by_row(row)
            users.append(u)
        return users

    def find_by_username(self, username):
        """Hae valmentaja käyttäjänimellä

        Returns:
            User-olio jos kyseinen valmentaja löytyy, muuten None
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE username =?", (username,)
        )

        row = cursor.fetchone()

        return create_user_by_row(row)


def create_user_by_row(row):
    if row:
        u = User(name=row["name"], team=row["team"],
                 username=row["username"], password=row["password"])
    else:
        u = None
    return u


USER_REPOSITORY = UserRepository(get_database_connection())
