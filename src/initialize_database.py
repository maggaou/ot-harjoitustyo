from database_connection import get_database_connection


def drop_tables(connection):
    """ Operaatio 1: poista taulut (Users)

    Args:
        connection: yhteys tietokantaan
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists Users;
    """)

    connection.commit()


def create_tables(connection):
    """Operaatio 2: taulujen luonti (Users)

    Args:
        connection: yhteys tietokantaan
    """

    cursor = connection.cursor()

    cursor.execute("""
        create table Users (
            name text,
            team text,
            username text primary key,
            password text
        );
    """)

    connection.commit()


def initialize_database():
    """Tietokannan alustus (operaatiot 1 ja 2)"""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
