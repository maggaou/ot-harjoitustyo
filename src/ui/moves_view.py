from tkinter import ttk, constants
from services.moves_service import MOVES_SERVICE as moves_service


class MovesListView:
    """Liikkeiden lista-näkymä."""

    def __init__(self, root, moves):
        """Luokan konstruktori.
        
        Args:
            root: tkinter ikkuna yms.
            moves: lista näkymän liikkeistä
        """

        self._root = root
        self._moves = moves
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for move in self._moves:
            self._initialize_move_item(move)

    def _initialize_move_item(self, move):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=move.name)

        label.grid(row=0, column=0, padx=10, pady=10)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pakc(fill=constants.X)
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()