from pathlib import Path
import caput
from config import MOVES_PATH
from entities.move import Move

class MovesRepository:
    """Liikkeiden tallennus tekstitiedostoina.
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
        """Tallenna liike tiedostoihin.
        """
        self.make_sure_that_directory_exists()

        file_path = Path(self.directory) / (move.id + ".md")
        metadata = dict(move.__dict__)
        content = metadata.pop("content")

        caput.write_contents(file_path, content, metadata)

        return move

    def find_all(self):
        """Palauttaa kaikki liikkeet.

        Returns:
            Lista (Move)
        """
        self.make_sure_that_directory_exists()
        moves = []

        for file in Path(self.directory).glob("*.md"):
            content = caput.read_contents(file)
            metadata = caput.read_config(file)
            args = dict(metadata)
            args["content"] = content
            moves.append(Move(**args))

        return moves

    def make_sure_that_directory_exists(self):
        path = Path(self.directory)
        if not path.exists():
            path.mkdir()




MOVES_REPOSITORY = MovesRepository(MOVES_PATH)
