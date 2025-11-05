class User:
    """Valmentajan tiedot

    Attributes:
        nimi: valmentajan koko nimi
        seura: valmentajan seura
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, name, team, username, password):
        self.name = name
        self.team = team
        self.username = username
        self.password = password