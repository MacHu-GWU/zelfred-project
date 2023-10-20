# -*- coding: utf-8 -*-

"""
User type query and return a dropdown list of suggestions. User can tab "Enter"
to Google search in web browser.

Dependencies:

.. code-block:: bash

    pip install requests

Demo: https://asciinema.org/a/616014
"""

import typing as T
import dataclasses
import xml.etree.ElementTree as ET

import requests
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
        zf.open_url(self.arg)


def encode_query(query: str) -> str:
    """
    Encode the query to be used in the url.
    """
    return query.replace(" ", "+")


class GoogleComplete:
    """
    Google complete API caller and parser.
    """

    google_complete_endpoint = (
        "https://www.google.com/complete/search?output=toolbar&q={query}"
    )

    def _encode_endpoint(self, query: str) -> str:
        """
        :return: full api url.
        """
        query = "+".join([s for s in query.split(" ") if s.strip()])
        return self.google_complete_endpoint.format(query=query)

    def _parse_response(self, html: str) -> T.List[str]:
        """
        :return: list of suggestions.
        """
        root = ET.fromstring(html)
        suggestion_list = list()
        for suggestion in root.iter("suggestion"):
            suggestion_list.append(suggestion.attrib["data"])
        return suggestion_list

    def get(self, query: str) -> T.List[str]:
        """
        :return: list of suggestions.
        """
        url = self._encode_endpoint(query)
        html = requests.get(url).text
        suggestion_list = self._parse_response(html)
        return suggestion_list


gc = GoogleComplete()


def convert_str_list_to_item_list(str_list: T.List[str]) -> T.List[Item]:
    """
    Convert a string list to a list of items. The string will become the
    title, uid, autocomplete and the arg.
    """
    return [
        Item(
            title=s,
            subtitle=f"hit 'Enter' to Google search {s!r} in web browser",
            uid=s,
            autocomplete=s,  # allow user to tap 'Tab' to auto-complete
            arg=f"https://www.google.com/search?q={encode_query(s)}",  # google search url
        )
        for s in str_list
    ]


def handler(query: str, ui: zf.UI):
    """
    Handler is the heart of a zelfred App. It is a user defined function that takes
    the entered query as input, and returns a list of items as output.
    """
    # if query is not empty
    if query:
        suggestion_list = gc.get(query)
        return convert_str_list_to_item_list(suggestion_list)
    # if query is empty, return the full list in the original order
    else:
        return [
            Item(
                title="type something to search in google",
            )
        ]


if __name__ == "__main__":
    # reset the debugger and enable it
    zf.debugger.reset()
    zf.debugger.enable()

    # create the UI and run it
    ui = zf.UI(handler=handler, capture_error=True)
    ui.run()
