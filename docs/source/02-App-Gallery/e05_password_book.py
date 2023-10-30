# -*- coding: utf-8 -*-

"""
User the user input to search the username, allow user to tap "Ctrl A" to copy
the password to clipboard. Afterward, the UI doesn't exit and wait for the next
user input.

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
from fuzzywuzzy import process
import zelfred.api as zf


@dataclasses.dataclass
class Item(zf.Item):
    """
    Define the custom item class because we need to override the ``enter_handler``.
    """

    copied: bool = dataclasses.field(default=False)

    def ctrl_a_handler(self, ui: zf.UI):
        """
        Copy the content to clipboard.
        """
        pyperclip.copy(self.arg)
        for item in ui.dropdown.items:
            item.subtitle = f"hit {ui.terminal.magenta}Ctrl A{ui.terminal.normal} to copy to clipboard"
        ui.dropdown.selected_item.subtitle = (
            f"{ui.terminal.green}Copied{ui.terminal.normal}"
        )

    def post_ctrl_a_handler(self, ui: zf.UI):
        ui.need_run_handler = False
        ui.need_move_to_end = False
        ui.need_clear_query = False
        ui.need_print_query = False


def encode_password(password: str) -> str:
    length = len(password)
    if length <= 8:
        return "*" * 12
    elif length <= 12:
        return password[:2] + "*" * 8 + password[-2:]
    else:
        return password[:4] + "*" * 4 + password[-4:]


def convert_user_pass_to_item_list(
    user_pwd_list: T.List[T.Tuple[str, str]],
) -> T.List[Item]:
    """
    Convert a list of username password pairs to a list of items.
    """
    return [
        Item(
            title=f"{user} = {encode_password(pwd)}",
            subtitle=f"hit {ui.terminal.magenta}Ctrl A{ui.terminal.normal} to copy to clipboard",
            uid=user,
            autocomplete=user,  # allow user to tap 'Tab' to auto-complete
            arg=pwd,  # the argument of the item will be used to copy to clipboard
        )
        for user, pwd in user_pwd_list
    ]


password_book = {
    "Google": "mygooglepassword",
    "Facebook": "myfacebookpassword",
    "Amazon": "myamazonpassword",
    "Apple": "myapplepassword",
    "Linkedin": "mylinedinassword",
    "Microsoft": "mymicrosoftassword",
}


def handler(query: str, ui: zf.UI):
    """
    Handler is the heart of a zelfred App. It is a user defined function that takes
    the entered query as input, and returns a list of items as output.
    """
    # if query is not empty
    if query:
        # sort by fuzzy match similarity
        results = process.extract(query, list(password_book), limit=len(password_book))
        return convert_user_pass_to_item_list(
            [(username, password_book[username]) for username, score in results]
        )
    # if query is empty, return the full list in the original order
    else:
        return convert_user_pass_to_item_list(
            [(k, v) for k, v in password_book.items()]
        )


if __name__ == "__main__":
    # reset the debugger and enable it
    zf.debugger.reset()
    zf.debugger.enable()

    # create the UI and run it
    ui = zf.UI(handler=handler, capture_error=True)
    ui.run()
