from tkinter import ttk, StringVar, constants
from services.moves_service import moves_service, InvalidCredentialsError

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

    