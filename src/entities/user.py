class User:
    """Valmentajan tiedot

    Attributes:
        name: valmentajan koko nimi
        team: valmentajan seura
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, name, team, username, password):
        self.name = name
        self.team = team
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.username == other.username