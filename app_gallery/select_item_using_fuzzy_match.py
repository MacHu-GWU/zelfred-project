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
from fuzzywuzzy import process
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


def convert_str_list_to_item_list(str_list: T.List[str]) -> T.List[Item]:
    """
    Convert a string list to a list of items. The string will become the
    title, uid, autocomplete and the arg.
    """
    return [
        Item(
            title=s,
            subtitle=f"hit 'Enter' to copy to clipboard",
            uid=s,
            autocomplete=s,  # allow user to tap 'Tab' to auto-complete
            arg=s,  # the argument of the item will be used to copy to clipboard
        )
        for s in str_list
    ]


zen_of_python = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
]


def handler(query: str, ui: zf.UI):
    """
    Handler is the heart of a zelfred App. It is a user defined function that takes
    the entered query as input, and returns a list of items as output.
    """
    # if query is not empty
    if query:
        # sort by fuzzy match similarity
        results = process.extract(query, zen_of_python, limit=len(zen_of_python))
        return convert_str_list_to_item_list([title for title, score in results])
    # if query is empty, return the full list in the original order
    else:
        return convert_str_list_to_item_list(zen_of_python)


if __name__ == "__main__":
    # reset the debugger and enable it
    zf.debugger.reset()
    zf.debugger.enable()

    # create the UI and run it
    ui = zf.UI(handler=handler, capture_error=True)
    ui.run()
