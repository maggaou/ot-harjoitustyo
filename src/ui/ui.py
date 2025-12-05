
from ui.create_move_view import CreateMoveView
from ui.edit_move_view import EditMoveView
from ui.login_view import LoginView
from ui.moves_view import MovesView
from ui.create_user_view import CreateUserView
from ui.show_move_view import ShowMoveView
from services.moves_service import moves_service


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
        self._show_moves_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_moves_view,
            self._show_create_user_view,
            self._show_moves_view
        )

        self._current_view.pack()

    def _show_moves_view(self):
        self._hide_current_view()

        self._current_view = MovesView(
            self._root,
            self._show_moves_view,
            self._show_create_move_view,
            self._show_login_view,
            self._show_move_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_moves_view,
            self._show_login_view,
            self._show_moves_view
        )

        self._current_view.pack()

    def _show_create_move_view(self):
        self._hide_current_view()

        self._current_view = CreateMoveView(
            self._root,
            self._show_moves_view,
            self._show_moves_view
        )

        self._current_view.pack()

    def _show_move_view(self, move_uid):
        move = moves_service.find_by_uid(move_uid)
        self._hide_current_view()

        self._current_view = ShowMoveView(
            self._root,
            move,
            self._show_moves_view,
            self._show_moves_view,
            self._show_edit_view,
        )

        self._current_view.pack()

    def _show_edit_view(self, move):
        self._hide_current_view()

        self._current_view = EditMoveView(
            self._root,
            move,
            self._show_move_view,
            lambda: self._show_move_view(move.uid),
        )

        self._current_view.pack()
