from tkinter import ttk, StringVar, constants
from services.moves_service import (
    moves_service,
    UsernameContainsSpacesError,
    UsernameExistsError,
    TooShortUsernameError,
    UsernameContainsCapitalLettersError,
    TooShortPasswordError,
    PasswordIsNonAsciiError,
)


class CreateUserView:
    """Rekisteröitymisen näkymä."""

    def __init__(self, root, handle_create_user, handle_show_login_view,
                 handle_show_moves_view):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_create_user: uuden käyttäjän luomisen toiminto.
            handle_show_login_view: kirjautumisen toiminto.
            handle_show_moves_view: näytä moves-näkymä.
        """

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_moves_view = handle_show_moves_view
        self._forms_frame = None
        self._instrucstions_frame = None
        self._base_frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None
        self._show_password_button = None
        self._initialize()

    def _initialize(self):
        self._base_frame = ttk.Frame(master=self._root)
        self._forms_frame = ttk.Frame(master=self._base_frame)
        self._instrucstions_frame = ttk.Frame(master=self._base_frame)

        # forms frame
        self._error_variable = StringVar(self._forms_frame)

        self._error_label = ttk.Label(
            master=self._forms_frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=10, pady=10)

        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            master=self._forms_frame,
            text="Create new user",
            command=self._create_user_handler
        )

        show_moves_button = ttk.Button(
            master=self._forms_frame,
            text="Show moves",
            command=self._handle_show_moves_view
        )

        or_label = ttk.Label(
            master=self._forms_frame,
            text="OR",
        )

        login_button = ttk.Button(
            master=self._forms_frame,
            text="Go to login",
            command=self._handle_show_login_view
        )

        self._forms_frame.grid_columnconfigure(0, weight=1, minsize=500)

        create_user_button.grid(padx=10, pady=5)
        or_label.grid(pady=5)
        login_button.grid(padx=10, pady=5)
        show_moves_button.grid(pady=5)

        self._hide_error()

        # instructions frame
        instructions_label_01 = ttk.Label(
            master=self._instrucstions_frame,
            text=(
                "Username requirements:\n"
                "- at lest 3 characters long\n"
                "- only lowercase letters\n"
                "- no spaces"
            )
        )
        instructions_label_02 = ttk.Label(
            master=self._instrucstions_frame,
            text=(
                "Password requirements:\n"
                "- must be at least 8 characters\n"
                "- only ASCII characters"
            )
        )
        self._show_password_button = ttk.Button(
            master=self._instrucstions_frame,
            text="Show password",
            command=self._show_password
        )

        instructions_label_01.grid(pady=15, sticky=constants.W)
        instructions_label_02.grid(pady=30, sticky=constants.W)

        self._show_password_button.grid(sticky=constants.W)

        # base frame
        self._instrucstions_frame.grid(
            row=0, column=0, padx=15, sticky=constants.W)
        self._forms_frame.grid(row=0, column=1, padx=0)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._forms_frame, text="Username")

        self._username_entry = ttk.Entry(master=self._forms_frame)

        username_label.grid(padx=10, pady=10)
        self._username_entry.grid(padx=10, pady=10)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._forms_frame, text="Password")

        self._password_entry = ttk.Entry(
            master=self._forms_frame,
            show='∗',
        )

        password_label.grid(padx=10, pady=10)
        self._password_entry.grid(padx=10, pady=10)

    def pack(self):
        """Näytä näkymä."""
        self._base_frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoa näkymä."""
        self._base_frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            moves_service.create_new_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} is already registered")
        except UsernameContainsSpacesError:
            self._show_error("Username: spaces are not allowed")
        except TooShortUsernameError:
            self._show_error("Username is too short")
        except UsernameContainsCapitalLettersError:
            self._show_error("Username: only small letters are allowed")
        except TooShortPasswordError:
            self._show_error("Password is too short")
        except PasswordIsNonAsciiError:
            self._show_error("Password has non-ASCII characters")

    def _show_password(self):
        if self._password_entry.cget('show') == '∗':
            self._password_entry.config(show='')
            self._show_password_button.config(text='Hide password')
        else:
            self._password_entry.config(show='∗')
            self._show_password_button.config(text='Show password')
