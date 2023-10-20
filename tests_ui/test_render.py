# -*- coding: utf-8 -*-

import pytest
import os
import time
import dataclasses
from fuzzywuzzy import process

from zelfred.item import Item
from zelfred.render import Render, UIRender, LineEditor, Dropdown
from zelfred.ui import UI


# ------------------------------------------------------------------------------
# Generic Render
# ------------------------------------------------------------------------------
def example1():
    render = Render()
    render.print_line("hello")
    assert render.line_number == 1
    assert render.n_lines == 1

    render.print_line("world")
    assert render.line_number == 2
    assert render.n_lines == 2

    time.sleep(1)


def example2():
    render = Render()
    render.print_str("alice, ")
    assert render.line_number == 0
    assert render.n_lines == 0

    render.print_str("bob, ")
    assert render.line_number == 0
    assert render.n_lines == 0

    render.print_str("cathy", new_line=True)
    assert render.line_number == 1
    assert render.n_lines == 1

    render.print_line("hello")
    assert render.line_number == 2
    assert render.n_lines == 2

    render.print_line("world")
    assert render.line_number == 3
    assert render.n_lines == 3

    time.sleep(1)

    render.move_to_start()
    assert render.line_number == 0
    assert render.n_lines == 3
    time.sleep(1)


def example3():
    render = Render()
    render.print_line("alice")
    render.print_line("bob")
    render.print_line("cathy")
    render.print_line("david")
    assert render.line_number == 4
    assert render.n_lines == 4
    time.sleep(1)

    render.clear_n_lines(1)
    assert render.line_number == 3
    assert render.n_lines == 3
    time.sleep(1)

    render.clear_n_lines(1)
    assert render.line_number == 2
    assert render.n_lines == 2
    time.sleep(1)

    render.clear_all()
    assert render.line_number == 0
    assert render.n_lines == 0
    time.sleep(1)


def example4():
    render = Render()
    render.print_line("alice")
    render.print_line("bob")
    render.print_line("cathy")
    render.print_line("david")
    assert render.line_number == 4
    assert render.n_lines == 4
    time.sleep(1)

    render.move_to_start()
    assert render.line_number == 0
    assert render.n_lines == 4
    time.sleep(1)


# ------------------------------------------------------------------------------
# UIRender
# ------------------------------------------------------------------------------
@dataclasses.dataclass
class MyItem(Item):
    def enter_handler(self, ui: UI):
        print(f"enter: {self.title}")


def get_items():
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
    items = [
        MyItem(
            uid=f"id-{str(ith).zfill(2)}",
            title=zen,
            subtitle=f"subtitle {str(ith).zfill(2)}",
            autocomplete=zen,
            arg=zen,
        )
        for ith, zen in enumerate(zen_of_python, start=1)
    ]
    return items


def handler(query: str):
    items = get_items()
    if query:
        mapper = {item.title: item for item in items}
        title_list = list(mapper.keys())
        result = process.extract(query, title_list, limit=len(items))
        return [mapper[title] for title, score in result]
    else:
        return items


def example5():
    ui_render = UIRender()

    query = ""
    le = LineEditor()
    le.enter_text(query)
    items = handler(query)
    dd = Dropdown(items=items)

    ui_render.print_ui(le, dd)
    time.sleep(1)

    ui_render.move_to_end()
    time.sleep(1)


def example6():
    ui_render = UIRender()
    query = ""
    le = LineEditor()
    le.enter_text(query)
    items = handler(query)
    dd = Dropdown(items=items)

    # print entire ui
    ui_render.print_ui(le, dd)
    time.sleep(1)

    # update line editor
    query = "simple"
    le.enter_text(query)
    ui_render.update_line_editor(le)
    ui_render.move_cursor_to_line_editor(le)
    time.sleep(1)

    # update dropdown
    items = handler(query)
    dd.update(items)
    ui_render.update_dropdown(dd, line_width=ui_render.terminal.width)
    time.sleep(1)

    # clear ui
    ui_render.clear_ui()
    time.sleep(1)


def test():
    print("")
    example1()
    example2()
    example3()
    example4()
    example5()
    example6()
    pass


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    pytest.main([abspath, "-s", "--tb=native"])


# manually run coverage test, remove the ``omit`` part in the ``.coveragerc`` file
# before running this
# if __name__ == "__main__":
#     from zelfred.tests import run_cov_test
#
#     run_cov_test(__file__, "zelfred.render", preview=True)
