from tkinter import Radiobutton, StringVar, ttk, constants
from tkinter import font
from datetime import datetime
from services.moves_service import moves_service


class MovesListView:
    """Liikkeiden listauksen näkymä.

    Attributes:
        moves: lista liikeistä (Move) jotka näytetään parhaillaan.
    """

    def __init__(self, root, moves, handle_show_move_view):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            moves: lista näkymän liikkeistä
            handle_show_move_view: yksittäisen liikkeen näkymä.

        """

        self.moves = moves
        self._root = root
        self._handle_show_move_view = handle_show_move_view
        self._frame = None

        self.initialize()

    def initialize(self):
        """Alusta moves-lista sen hetkisillä liikkeillä."""

        bold_font = font.Font(family="Helvetica", size=13, weight="bold")
        self._frame = ttk.Frame(master=self._root)
        added_label = ttk.Label(
            master=self._frame,
            text="Added",
            font=bold_font,
        )
        modified_label = ttk.Label(
            master=self._frame,
            text="Modified",
            font=bold_font,
        )
        name_label = ttk.Label(
            master=self._frame,
            text="Name",
            font=bold_font,
        )
        added_label.grid(row=0, column=0, padx=20, sticky=constants.W)
        modified_label.grid(row=0, column=1, padx=20, sticky=constants.W)
        name_label.grid(row=0, column=2, padx=20, sticky=constants.W)

        for row, move in enumerate(self.moves):
            self._initialize_move_item(move, row+1)

    def _initialize_move_item(self, move, row):
        underline_font = font.Font(family="Helvetica", size=13, underline=True)
        normal_font = font.Font(family="Helvetica", size=13)
        name_label = ttk.Label(
            master=self._frame,
            text=move.name,
            foreground="cyan",
            cursor="cross",
            font=underline_font
        )

        name_label.grid(row=row, column=2, padx=20, pady=5, sticky=constants.W)
        name_label.bind(
            "<Button-1>", lambda event: self._handle_show_move_view(move.uid))

        modified_label = ttk.Label(
            master=self._frame,
            text=move.modifications[-1][0] if move.modifications else "-",
            foreground="cyan",
            font=normal_font,
        )
        modified_label.grid(row=row, column=1, padx=20,
                            pady=5, sticky=constants.W)

        added_label = ttk.Label(
            master=self._frame,
            text=move.date_submitted,
            foreground="cyan",
            font=normal_font,
        )
        added_label.grid(row=row, column=0, padx=20,
                         pady=5, sticky=constants.W)

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(padx=10, pady=12)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()


class MovesView:
    """Liikkeiden listanäkymä ja muut toiminnot."""

    def __init__(self, root, handle_logout, handle_create_move,
                 handle_show_login, handle_show_move_view):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_logout: näkymä uloskirjautumisen jälkeen.
            handle_create_move: näkymä kun käyttäjä painaa create move.
            handle_show_login: palaaminen takaisin login-näkymään.
            handle_show_move_view: yksittäisen liikkeen näkymä.
        """
        self._root = root
        self._handle_logout = handle_logout
        self._handle_create_move = handle_create_move
        self._handle_show_login = handle_show_login
        self._handle_show_move_view = handle_show_move_view
        self._user = moves_service.get_logged_in_user()
        self._sort_var = None
        self._frame = None
        self._moves_list_frame = None
        self._moves_list_view = None

        self._initialize()

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()

    def _logout_handler(self):
        moves_service.logout()
        self._handle_logout()

    def _initialize_moves_list(self, reorder=False):
        if self._moves_list_view:
            self._moves_list_view.destroy()

        sort = {
            "added": lambda x: datetime.strptime(x.date_submitted, "%d.%m.%Y %H:%M:%S"),
            "name": lambda x: x.name,
            "modified": lambda x: (
                datetime.strptime(x.modifications[-1][0], "%d.%m.%Y %H:%M:%S")
                if x.modifications
                else
                datetime.strptime(x.date_submitted, "%d.%m.%Y %H:%M:%S")
            )
        }
        if not reorder:
            moves = moves_service.return_all()
        else:
            moves = self._moves_list_view.moves
        if not moves:
            self._moves_list_view = ttk.Label(
                self._moves_list_frame,
                text="No moves created yet",
            )
            self._moves_list_view.pack()
            return

        moves.sort(key=sort[self._sort_var.get()])

        if not reorder:
            self._moves_list_view = MovesListView(
                self._moves_list_frame,
                moves,
                self._handle_show_move_view,
            )
        else:
            self._moves_list_view.initialize()

        self._moves_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user}" if self._user else "Not logged in"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        create_move_button = ttk.Button(
            master=self._frame,
            text="Create new",
            command=self._handle_create_move
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login/Create account",
            command=self._handle_show_login
        )
        user_label.grid(row=0, column=0, padx=10, pady=10)

        self._sort_var = StringVar(master=self._frame, value="added")

        sort_frame = ttk.Frame(master=self._frame)

        sort_label = ttk.Label(
            master=sort_frame,
            text="Select sort:",
        )

        sort_label.pack(side=constants.LEFT)

        for sort in ["added", "name", "modified"]:
            Radiobutton(
                master=sort_frame,
                text=sort,
                value=sort,
                variable=self._sort_var,
                command=lambda: self._initialize_moves_list(True),
            ).pack(side=constants.LEFT)

        sort_frame.grid(row=1, padx=10, sticky=constants.W)

        if self._user:
            logout_button.grid(
                row=0,
                column=1,
                padx=10,
                pady=10
            )

            create_move_button.grid(
                row=0,
                column=2,
                padx=10,
                pady=10
            )
        else:
            login_button.grid(
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
            row=2,
            column=0,
            sticky=constants.W,
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
