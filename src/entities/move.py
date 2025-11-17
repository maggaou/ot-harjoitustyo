import uuid


class Move():
    """ Yksittäinen painiliike.

    Attributes:
        name: liikkeen nimi
        style: painimuoto (WW, FS, GR)
        age_group: ikäryhmä (6+, 12+, 16+)
        difficulty: vaikeusaste (basic, intermediate, advanced)
        orginal_creator: alkuperäinen lisääjä (User)
        date_submitted: milloin luotu
        content: sisältö
        picture_link: ulkoinen linkki kuvaan
        reference: ulkoinen linkki
    """

    def __init__(self, content, name=None, style=None, age_group=None,
                 difficulty=None, original_creator=None, date_submitted=None,
                 picture_link=None, reference=None, uid=None):
        """Luokan konstruktori.

        Args:
            name: liikkeen nimi
            style: painimuoto (Style.GR jne)
            age_group: ikäryhmä (AgeGroup.SIX jne)
            difficulty: vaikeusaste (Difficulty.BASIC jne)
            orginal_creator: liikkeen alkuperäinen lisääjä
            date_submitted: milloin liike on lisätty
            content: sisältö (markdown muotoilu)
            picture_link:
                Valinnainen, oletusarvo None
                Ulkoinen linkki kuvaan (string)
            reference: 
                Valinnainen, oletusarvo None
                Ulkoinen linkki jos käytössä on lähdevideo jne (string)
        """

        self.name = name
        self.style = style
        self.age_group = age_group
        self.difficulty = difficulty
        self.original_creator = original_creator
        self.date_submitted = date_submitted
        self.content = content
        self.picture_link = picture_link
        self.reference = reference

        self.id = uid or str(uuid.uuid4())

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return other.id == self.id
