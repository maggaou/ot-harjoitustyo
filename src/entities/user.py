class User:
    """Valmentajan tiedot.

    Attributes:
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, username=None, password=None):
        """Luokan konstruktori.

        Args:
            username (str, optional): käyttäjätunnus. Defaults to None.
            password (str, optional): salasana. Defaults to None.
        """
        self.username = username
        self.password = password

    def __eq__(self, other):
        """Käyttäjän yhtäsuuruus käyttäjänimien perusteella.

        Args:
            other (User): vertailtava käyttäjä.

        Returns:
            bool: True jos käyttäjänimet ovat samat, muuten False
        """

        if not isinstance(other, User):
            return False
        return self.username == other.username
