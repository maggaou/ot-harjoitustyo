class User:
    """Valmentajan tiedot.

    Attributes:
        name: valmentajan koko nimi
        team: valmentajan seura
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, name=None, team=None, username=None, password=None):
        """Luokan konstruktori.

        Args:
            name (str, optional): valmentajan koko nimi. Defaults to None.
            team (str, optional): valmentajan seura. Defaults to None.
            username (str, optional): käyttäjätunnus. Defaults to None.
            password (str, optional): salasana. Defaults to None.
        """
        self.name = name
        self.team = team
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

    def __repr__(self):
        """Käyttäjän merkkijonoesitys käyttäjänimen perusteella."""

        return self.username
