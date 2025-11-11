
from ui.login_view import LoginView
from ui.moves_view import MovesListView
from ui.create_user_view import CreateUserView

class UI:
    """Sovelluksen käyttöliittymä."""

    def __init__(self, root):
        """Luokan konstruktori.
        
        Args:
            root: tkinter ikkuna.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käyttöliittymän käynnistys."""
        self._show_login_view()
    

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_moves_view,
            self._show_create_user_view
        )
    
    def _show_moves_view(self):
        self._hide_current_view()

        self._current_view = MovesListView(self._root, self._show_login_view)

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_moves_view,
            self._show_login_view
        )

        self._current_view.pack()