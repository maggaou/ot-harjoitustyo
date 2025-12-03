from tkinter import StringVar, font, ttk, constants
import requests
from requests import exceptions
from PIL import Image, ImageTk, UnidentifiedImageError
from services.moves_service import moves_service
from entities.move import Move

class ShowMoveView:
    """Yksittäisen liikkeen näkymä."""

    def __init__(self, root, move, handle_show_moves, handle_delete_move, handle_edit_move):
        """Luokan konstruktori.

        Args:
            root: tkinter ikkuna yms.
            move: näytettävä liike.
            handle_show_moves: paluu takaisin päänäkymään.
            handle_delete_move: paluu takaisin päänäkymään.
            handle_edit_move: avaa liikkeen muokkaaminen.
        """

        self._root = root
        self._move = move
        self._handle_show_moves = handle_show_moves
        self._handle_delete_move = handle_delete_move
        self._handle_edit_move = lambda: handle_edit_move(move)
        self._frame = None
        self._photo = None
        self._photo_frame = None
        self._data_frame = None
        self._error_label = None
        self._error_text = None
        self._initialize()

    def pack(self):
        """Näkymän näyttäminen."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Näkymän tuhoaminen."""
        self._frame.destroy()

    def _initialize_rows(self):
        bold_font = font.Font(family="Helvetica", size=13, weight="bold")
        normal_font = font.Font(family="Helvetica", size=13)
        underline_font = font.Font(family="Helvetica", size=13, underline=True)

        move_dict = vars(self._move)
        move_dict_sorted = {key: move_dict[key]
                            for key in sorted(move_dict, key=Move.order)}
        for i, field in enumerate(move_dict_sorted):
            text_field_name = field.capitalize().replace('_', ' ') + ":"
            text_field_value = move_dict[field]

            field_name_label = ttk.Label(
                self._data_frame, text=text_field_name, font=bold_font, foreground="cyan")

            field_value_frame = ttk.Frame(self._data_frame)

            if isinstance(text_field_value, str):
                field_value_label = ttk.Label(
                    field_value_frame,
                    text=text_field_value,
                    font=normal_font,
                    wraplength=350,
                )
                field_value_label.grid()
            if isinstance(text_field_value, list):
                for k, item in enumerate(text_field_value):
                    current_username = ""
                    if moves_service.get_logged_in_user():
                        current_username = moves_service.get_logged_in_user().username
                    field_value_label = ttk.Label(
                        field_value_frame,
                        font=normal_font if item[1] != current_username else underline_font,
                        text=" ".join(item),
                    )
                    field_value_label.grid(row=k, sticky=constants.W)

            field_name_label.grid(row=i, column=0, pady=5, sticky=constants.NE)
            field_value_frame.grid(row=i, column=1, pady=5, sticky=constants.W)

        return len(move_dict)

    def _delete_move(self):
        moves_service.delete_move(self._move)
        self._handle_delete_move()

    @staticmethod
    def _load_image_from_url(url):
        image = Image.open(requests.get(url, stream=True, timeout=0.5).raw)
        width, height = image.size
        new_width = 300
        new_height = int((new_width / width) * height)
        image = image.resize((new_width, new_height))
        return image

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._data_frame = ttk.Frame(master=self._frame)
        self._photo_frame = ttk.Frame(master=self._frame)

        normal_font = font.Font(family="Helvetica", size=13)

        self._error_text = StringVar(self._photo_frame)
        self._error_label = ttk.Label(
            master=self._photo_frame,
            textvariable=self._error_text,
            font=normal_font,
        )

        final_row = self._initialize_rows()

        show_moves_button = ttk.Button(
            master=self._data_frame,
            text="Back",
            command=self._handle_show_moves
        )

        delete_move_button = ttk.Button(
            master=self._data_frame,
            text="Delete",
            command=self._delete_move,
        )

        modify_move_button = ttk.Button(
            master=self._data_frame,
            text="Edit",
            command=self._handle_edit_move,
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        show_moves_button.grid(row=final_row, column=0, pady=10)

        if moves_service.get_logged_in_user():
            delete_move_button.grid(row=final_row, column=1,
                                    pady=5, padx=30, sticky=constants.E)
            modify_move_button.grid(row=final_row+1, column=1,
                                    pady=5, padx=30, sticky=constants.E)
        
        self._photo_frame.grid(row=0, column=0, sticky=constants.W)
        self._data_frame.grid(row=0, column=1,sticky=constants.NW)
        
        if not self._move.picture_link:
            self._error_text.set("No image to display")
            self._error_label.pack()
            return
    
        try:
            image_pil = self._load_image_from_url(self._move.picture_link)
            self._photo = ImageTk.PhotoImage(image_pil)
            
            image_label = ttk.Label(master=self._photo_frame, image=self._photo)
            image_label.pack()
        except exceptions.MissingSchema:
            self._error_text.set("Invalid URL: no scheme supplied")
            self._error_label.pack()
        except exceptions.InvalidURL:
            self._error_text.set("Invalid URL: no host supplied")
            self._error_label.pack()
        except exceptions.ConnectionError:
            self._error_text.set("Invalid URL: connection error")
            self._error_label.pack()
        except UnidentifiedImageError:
            self._error_text.set("Invalid URL: not an image file")
            self._error_label.pack()
        except exceptions.ReadTimeout:
            self._error_text.set("Image read timed out. (read timeout=0.5)")
            self._error_label.pack()
