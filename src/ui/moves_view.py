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
        item_frame.pack(fill=constants.X)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


class MovesView:
    """Liikkeiden listanäkymä ja muut toiminnot."""

    def __init__(self, root, handle_logout):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_logout: näkymä uloskirjautumisen jälkeen.
        """
        self._root = root
        self._handle_logout = handle_logout
        self._user = moves_service.get_logged_in_user()
        self._frame = None
        self._moves_list_frame = None
        self._moves_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        moves_service.logout()
        self._handle_logout()

    def _initialize_moves_list(self):
        if self._moves_list_view:
            self._moves_list_view.destroy()

        moves = moves_service.return_all()

        self._moves_list_view = MovesListView(
            self._moves_list_frame,
            moves
        )

        self._moves_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=10, pady=10)

        logout_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._moves_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_moves_list()

        self._moves_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
