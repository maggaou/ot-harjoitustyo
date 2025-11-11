from tkinter import ttk, StringVar, constants
from services.moves_service import MOVES_SERVICE as moves_service, InvalidCredentialsError

class LoginView:
    """Kirjautumisen näkymä."""

    def __init__(self, root, handle_login, handle_show_create_user_view):
        """Luokan konstruktori.
        
        Args:
            root: tkinter ikkuna.
            handle_login: sisäänkirjautumisen toiminto.
            handle_show_create_user_view: uuden käyttäjän luomisen toiminto.
        """

        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            foreground = "red"
        )

        self._error_label.grid(padx=10, pady=10)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master = self._frame,
            text = "Login",
            command = self._login_handler
        )

        create_user_button = ttk.Button(
            master = self._farme,
            text = "Create user",
            command = self._handle_show_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize = 500)

        login_button.grid(padx=10, pady=10)
        create_user_button.grid(padx=10, pady=10)

        self._hide_error()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=10, pady=10)
        self._username_entry.grid(padx=10, pady=10)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=10, pady=10)

        self._password_entry.grid(padx=10, pady=10)

    def pack(self):
        self._frame.pack(fill=constants.x)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            moves_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")