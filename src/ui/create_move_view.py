from datetime import datetime
from services.moves_service import MoveNameIsEmptyError, moves_service
from ui.abstract_create_move import AbstractCreateMoveView


class CreateMoveView(AbstractCreateMoveView):
    """Liikkeiden lisäämisen näkymä."""

    def __init__(self, root, handle_create_move, handle_show_moves):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            handle_create_move: näkymä tai toiminto liikkeen luomisen jälkeen.
            handle_show_moves: palaaminen takaisin päänäkymään.
        """
        super().__init__(root, handle_create_move, handle_show_moves, "Create")

    def _form_action_handler(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d.%m.%Y")
        original_creator = moves_service.get_logged_in_user().username
        args = {"original_creator": original_creator,
                "date_submitted": formatted_date}

        args["name"] = self._entries["name"].get()
        args["content"] = self._entries["content"].get()
        args["style"] = self._entries["style"].get()
        args["age_group"] = self._entries["age_group"].get()
        args["difficulty"] = self._entries["difficulty"].get()
        args["picture_link"] = self._entries["picture_link"].get()
        args["reference"] = self._entries["reference"].get()

        try:
            moves_service.create_move(**args)
            self._handle_action()
        except MoveNameIsEmptyError:
            self._show_error("Move name cannot be empty")
