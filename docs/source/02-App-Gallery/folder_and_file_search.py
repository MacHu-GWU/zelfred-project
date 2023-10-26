# -*- coding: utf-8 -*-

"""
User can search folder in a root directory, and then tap "Enter" to enter
a sub query session to search file in the selected folder. At the end, user
can tab "Enter" to open the file using the default application.

Dependencies:

.. code-block:: bash

    pip install fuzzywuzzy
    pip install python-Levenshtein

Demo: https://asciinema.org/a/616119
"""

import typing as T
import dataclasses
from pathlib import Path

from fuzzywuzzy import process
import zelfred.api as zf


@dataclasses.dataclass
class FileItem(zf.Item):
    """
    Represent a file in the dropdown menu.
    """

    @classmethod
    def from_names(cls, name_list: T.List[str], folder: str) -> T.List["FileItem"]:
        """
        Convert a file name list to a list of items. The file name
        will become the title, uid, autocomplete and the arg.
        """
        return [
            cls(
                uid=name,
                title=name,
                subtitle=f"hit 'Enter' to open this file",
                arg=str(dir_home.joinpath(folder, name)),
                autocomplete=name,
            )
            for name in name_list
        ]

    def enter_handler(self, ui: zf.UI):
        """
        Open file in default application.
        """
        zf.open_file(Path(self.arg))


@dataclasses.dataclass
class FolderItem(zf.Item):
    """
    Represent a folder in the dropdown menu.
    """

    @classmethod
    def from_names(cls, name_list: T.List[str]) -> T.List["FolderItem"]:
        """
        Convert a folder name list to a list of items. The folder name
        will become the title, uid, autocomplete and the arg.
        """
        return [
            cls(
                title=name,
                subtitle=f"hit 'Enter' to search file in this folder",
                uid=name,
                autocomplete=name,  # allow user to tap 'Tab' to auto-complete
                arg=name,  # the argument of the folder item will be used to list files
            )
            for name in name_list
        ]

    def enter_handler(self, ui: zf.UI):
        """
        Enter a sub query session.
        """
        # list files in the selected folder
        folder = self.arg
        dir_folder = dir_home.joinpath(self.arg)
        file_list = [file.name for file in dir_folder.iterdir()]
        ui.run_handler(items=FileItem.from_names(file_list, folder))

        # re-paint the UI
        ui.line_editor.clear_line()
        ui.move_to_end()
        ui.clear_items()
        ui.clear_query()
        ui.print_query()
        ui.print_items()

        # enter the main event loop of the sub query
        # user can tap 'F1' to exit the sub query session,
        # and go back to the folder selection session.
        def handler(query: str, ui: zf.UI):
            """
            A partial function that using the given folder.
            """
            return handler_file(folder, query, ui)

        ui.replace_handler(handler)
        ui.run(_do_init=False)


dir_home = Path(__file__).absolute().parent.joinpath("home")


def handler_file(folder: str, query: str, ui: zf.UI):
    """
    This is the handler for the sub query session.

    Given a folder, you have to create a partial function that using the given
     folder. The partial function will become the final handler of the sub query.
    """
    file_list = [p.name for p in dir_home.joinpath(folder).iterdir()]
    # if query is not empty
    if query:
        # sort by fuzzy match similarity
        results = process.extract(query, file_list, limit=len(file_list))
        return FileItem.from_names([file for file, score in results], folder)
    # if query is empty, return the full list in the original order
    else:
        return FileItem.from_names(file_list, folder)


def handler_folder(query: str, ui: zf.UI):
    """
    Handler is the heart of a zelfred App. It is a user defined function that takes
    the entered query as input, and returns a list of items as output.
    """
    folder_list = [p.name for p in dir_home.iterdir()]
    # if query is not empty
    if query:
        # sort by fuzzy match similarity
        results = process.extract(query, folder_list, limit=len(folder_list))
        return FolderItem.from_names([folder for folder, score in results])
    # if query is empty, return the full list in the original order
    else:
        return FolderItem.from_names(folder_list)


if __name__ == "__main__":
    # reset the debugger and enable it
    zf.debugger.reset()
    zf.debugger.enable()

    # create the UI and run it
    ui = zf.UI(handler=handler_folder, capture_error=True)
    ui.run()
