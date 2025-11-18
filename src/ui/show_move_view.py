from tkinter import ttk, constants


class ShowMoveView:
    """Yksittäisen liikkeen näkymä."""

    def __init__(self, root, move, handle_show_moves):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            move: näytettävä liike.
            handle_show_moves: paluu takaisin päänäkymään.
        """

        self._root = root
        self._move = move
        self._handle_show_moves = handle_show_moves
        self._frame = None

        self._initialize()

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()

    def _initialize_rows(self):
        move_dict = vars(self._move)
        for i, L in enumerate(move_dict):
            text = L.capitalize().replace('_', ' ') + ": " + move_dict[L]
            label = ttk.Label(self._frame, text=text)
            label.grid(row=i, pady=5)
        return len(move_dict)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        final_row = self._initialize_rows()

        show_moves_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_show_moves
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        show_moves_button.grid(row=final_row, pady=10)
