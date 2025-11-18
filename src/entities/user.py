class User:
    """Valmentajan tiedot

    Attributes:
        name: valmentajan koko nimi
        team: valmentajan seura
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, name=None, team=None, username=None, password=None):
        self.name = name
        self.team = team
        self.username = username
        self.password = password

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username

    def __repr__(self):
        return self.username
