from pathlib import Path

from config import MOVES_PATH
from entities.move import Move


class MovesRepository:
    """Liikkeiden tallennus tekstitiedostoina
    """

    def __init__(self, directory):
        """Luokan konstruktori
        
        Args:
            directory: kansio johon tekstitiedostot tallennetaan
        """

        self.directory = directory

    def delete_all(self):
        self.make_sure_that_directory_exists()
        for file in Path(self.directory).glob("*.md"):
            file.unlink()

    def create(self, move):
        self.make_sure_that_directory_exists()

        file_path = Path(self.directory) / (move.id + ".md")
        file_path.write_text(move.content, encoding="utf-8")

    def find_all(self):
        """Palauttaa kaikki liikkeet

        Returns:
            Lista (Move)
        """
        self.make_sure_that_directory_exists()
        moves = list()

        for file in Path(self.directory).glob("*.md"):
            content = file.read_text(encoding="utf-8")
            moves.append(Move(content = content))

        return moves

    def make_sure_that_directory_exists(self):
        path = Path(self.directory)
        if not path.exists():
            path.mkdir()


MOVES_REPOSITORY = MovesRepository(MOVES_PATH)