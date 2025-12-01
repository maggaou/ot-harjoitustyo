from tkinter import StringVar, font, ttk, constants
from abc import ABC, abstractmethod


class AbstractCreateMoveView(ABC):
    """Liikkeiden lisäämisen tai muokkaamisen näkymä."""

    def __init__(self, root, handle_action, handle_show_moves, action):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_action: näkymä luomisen/muokkaamisen jälkeen.
            handle_show_moves: palaaminen takaisin päänäkymään.
            action: näkymän toiminto (teksti).
        """

        self._root = root
        self._handle_action = handle_action
        self._handle_show_moves = handle_show_moves
        self._frame = None
        self._entries = {}
        self._action_button_text = action
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()

    def _go_to_back_handler(self):
        self._handle_show_moves()

    @abstractmethod
    def _form_action_handler(self):
        pass

    def _initialize_fields(self):
        fields = ["name", "content", "style", "age_group",
                  "difficulty", "picture_link", "reference"]

        for i, f in enumerate(fields):
            label_text = f.capitalize().replace('_', ' ')
            label = ttk.Label(master=self._frame, text=label_text)

            self._entries[f] = ttk.Entry(master=self._frame)

            label.grid(row=i+1, column=0, padx=5, pady=5)
            self._entries[f].grid(row=i+1, column=1, padx=5, pady=5)

        return len(fields)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        error_font = font.Font(family="Helvetica", size=16)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            font=error_font,
            foreground="red",
        )

        self._error_label.grid(row=0, column=1, padx=10, pady=10)

        r = self._initialize_fields() + 1

        action_button = ttk.Button(
            master=self._frame,
            text=self._action_button_text,
            command=self._form_action_handler
        )

        go_to_moves_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_to_back_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        go_to_moves_button.grid(row=r, column=0, padx=5, pady=5)
        action_button.grid(row=r, column=1, padx=5, pady=5)

        self._hide_error()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()
