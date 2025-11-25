from services.moves_service import moves_service
from ui.abstract_create_move import AbstractCreateMoveView


class EditMoveView(AbstractCreateMoveView):
    def __init__(self, root, move, handle_edit_move, handle_show_moves):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            move: muokattava liike (Move-objekti)
            handle_edit_move: näkymä tai toiminto liikkeen muokkaamisen jälkeen.
            handle_show_moves: palaaminen takaisin päänäkymään.
        """
        super().__init__(root, lambda: handle_edit_move(
            move.uid), handle_show_moves, "Confirm")
        self.move = move

    def _form_action_handler(self):
        args = dict(vars(self.move))
        args["name"] = self._entries["name"].get()
        args["content"] = self._entries["content"].get()
        args["style"] = self._entries["style"].get()
        args["age_group"] = self._entries["age_group"].get()
        args["difficulty"] = self._entries["difficulty"].get()
        args["picture_link"] = self._entries["picture_link"].get()
        args["reference"] = self._entries["reference"].get()

        moves_service.edit_move(**args)
        self._handle_action()

    def _prefill_entries(self):
        move_dict = vars(self.move)
        for f, entry in self._entries.items():
            entry.insert(0, move_dict[f])

    def pack(self):
        super().pack()
        self._prefill_entries()
