class User:
    """Valmentajan tiedot

    Attributes:
        nimi: valmentajan koko nimi
        seura: valmentajan seura
        username: käyttäjätunnus
        password: salasana
    """

    def __init__(self, nimi, seura, username, password):
        self.nimi = nimi
        self.seura = seura
        self.username = username
        self.password = password