from tkinter import font, ttk, constants
from services.moves_service import moves_service

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
        bold_font = font.Font(family="Helvetica", size=13, weight="bold")
        normal_font = font.Font(family="Helvetica", size=13, weight="normal")

        move_dict = vars(self._move)

        for i, field in enumerate(move_dict):
            text_field_name = field.capitalize().replace('_', ' ') + ":"
            text_field_value = move_dict[field]

            field_name_label = ttk.Label(
                self._frame, text=text_field_name, font=bold_font, foreground="cyan")
            field_value_label = ttk.Label(
                self._frame, text=text_field_value, font=normal_font)

            field_name_label.grid(row=i, column=0, pady=5, sticky=constants.E)
            field_value_label.grid(row=i, column=1, pady=5, sticky=constants.W)

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
