# -*- coding: utf-8 -*-

"""
Use the user input to sort a list of items by fuzzy match similarity.
Allow user to tap "Enter" to copy the content to clipboard.

Dependencies:

.. code-block:: bash

    pip install fuzzywuzzy
    pip install python-Levenshtein
    pip install pyperclip

Demo: https://asciinema.org/a/615992
"""

import typing as T
import dataclasses

import pyperclip
import zelfred.api as zf


@dataclasses.dataclass
class Item(zf.Item):
    """
    Define the custom item class because we need to override the ``enter_handler``.
    """

    def enter_handler(self, ui: zf.UI):
        """
        Copy the content to clipboard.
        """
        pyperclip.copy(self.arg)

    def post_enter_handler(self, ui: zf.UI):
        # print(ui.render)
        ui.need_run_handler = False
        ui.need_move_to_end = False
        ui.need_clear_items = False
        ui.need_clear_query = False
        ui.need_print_query = False
        ui.need_print_items = False
        # raise zf.exc.EndOfInputError(selection=self)


def convert_kv_list_to_item_list(kv_list: T.List[T.Tuple[str, str]]) -> T.List[Item]:
    """
    Convert a string list to a list of items. The string will become the
    title, uid, autocomplete and the arg.
    """
    return [
        Item(
            title=f"{k} = {v}",
            subtitle=f"hit 'Enter' to copy to clipboard",
            uid=k,
            autocomplete="",  # allow user to tap 'Tab' to auto-complete
            arg=k,  # the argument of the item will be used to copy to clipboard
        )
        for k, v in kv_list
    ]


password_book = [
    ("username 1", "password 1"),
    ("username 2", "password 2"),
    ("username 3", "password 3"),
]


def handler(query: str, ui: zf.UI):
    """
    Handler is the heart of a zelfred App. It is a user defined function that takes
    the entered query as input, and returns a list of items as output.
    """
    return convert_kv_list_to_item_list(password_book)


if __name__ == "__main__":
    # reset the debugger and enable it
    zf.debugger.reset()
    zf.debugger.enable()

    # create the UI and run it
    ui = zf.UI(handler=handler, capture_error=True, quit_on_action=False)
    ui.run()
