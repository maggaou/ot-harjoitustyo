

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
    

