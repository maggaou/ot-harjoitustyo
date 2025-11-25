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
        self.make_sure_that_directory_exists()

    def delete_all(self):
        """ Poista kaikki paikallisesti tallennetut liikkeet.
        """
        for file in Path(self.directory).glob("*.md"):
            file.unlink()

    def delete(self, move):
        """ Poista yksittäinen liike.

        Args:
            move: move-objekti.
        """
        file_path = Path(self.directory) / (move.uid + ".md")
        file_path.unlink()

    def create(self, move):
        """Tallenna liike tiedostoihin.
        """
        file_path = Path(self.directory) / (move.uid + ".md")
        metadata = dict(move.__dict__)
        content = metadata.pop("content")

        caput.write_contents(file_path, content, metadata)

        return move

    def modify(self, move):
        """Tallenna muokattu versio annetusta Move-objektista.
        
        Args:
            move: Move-objekti joka sisältää muokkaukset.
        """
        file_path = Path(self.directory) / (move.uid + ".md")
        metadata = dict(move.__dict__)
        content = metadata.pop("content")

        caput.write_contents(file_path, content, metadata)
    
    def find_by_uid(self, uid):
        """Hae move-objekti uid:n perusteella.
        
        Args:
            uid: haettavan move-objektin tunniste.
        Returns:
            haettu move-objekti.
        """
        file_path = Path(self.directory) / (uid + ".md")
        content = caput.read_contents(file_path)
        metadata = caput.read_config(file_path)
        args = dict(metadata)
        args["content"] = content

        return Move(**args)

    def find_all(self):
        """Palauttaa kaikki liikkeet.

        Returns:
            Lista (Move)
        """
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


moves_repository = MovesRepository(MOVES_PATH)
