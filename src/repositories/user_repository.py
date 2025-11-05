

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
            "insert into Users (name, team, username, password) values (?, ?, ?, ?)",
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

        cursor.execute("select * from Users")

        rows = cursor.fetchall()

        users = list()
        for row in rows:
            if row:
                u = User(name=row["name"], team=row["team"], 
                        username=row["username"], password=row["password"])
                users.append(u)
        
        return users

USER_REPOSITORY = UserRepository(get_database_connection())