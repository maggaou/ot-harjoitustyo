from datetime import datetime
from tkinter import ttk, constants
from services.moves_service import MOVES_SERVICE as moves_service


class CreateMoveView:
    """Liikkeiden lisäämisen näkymä."""

    def __init__(self, root, handle_create_move, handle_show_moves):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_create_move: näkymä tai toiminto liikkeen luomisen jälkeen.
            handle_show_moves: palaaminen takaisin päänäkymään.
        """

        self._root = root
        self._handle_create_move = handle_create_move
        self._handle_show_moves = handle_show_moves
        self._frame = None
        self._entries = {}

        self._initialize()

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()

    def _create_move_handler(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d.%m.%y")
        original_creator = moves_service.get_logged_in_user().username
        args = {"original_creator": original_creator,
                "date_submitted": formatted_date}

        args["name"] = self._entries["name"].get()
        args["content"] = self._entries["content"].get()
        args["style"] = self._entries["style"].get()
        args["age_group"] = self._entries["age_group"].get()
        args["difficulty"] = self._entries["difficulty"].get()
        args["picture_link"] = self._entries["picture_link"].get()
        args["reference"] = self._entries["reference"].get()

        moves_service.create_move(**args)
        self._handle_create_move()

    def _go_to_back_handler(self):
        self._handle_show_moves()

    def _initialize_fields(self):
        fields = ["name", "content", "style", "age_group",
                  "difficulty", "picture_link", "reference"]

        for i, f in enumerate(fields):
            label_text = f.capitalize().replace('_', ' ')
            label = ttk.Label(master=self._frame, text=label_text)

            self._entries[f] = ttk.Entry(master=self._frame)

            label.grid(row=i, column=0, padx=5, pady=5)
            self._entries[f].grid(row=i, column=1, padx=5, pady=5)

        return len(fields)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)

        r = self._initialize_fields()

        create_move_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_move_handler
        )

        go_to_moves_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_to_back_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        go_to_moves_button.grid(row=r, column=0, padx=5, pady=5)
        create_move_button.grid(row=r, column=1, padx=5, pady=5)
