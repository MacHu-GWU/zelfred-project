# -*- coding: utf-8 -*-

from zelfred.item import Item
from zelfred.render import UIRender, LineEditor, Dropdown

class TestRender:
    def test(self):
        print("")

        # r = UIRender()
        # assert r.n_lines == 0
        # assert r.line_number == 0
        #
        # line_editor = LineEditor()
        # line_editor.enter_text("Hello")
        # r.print_line_editor(line_editor)
        # assert r.n_lines == 1
        # assert r.line_number == 1
        #
        # dropdown = Dropdown(items=[Item(title="item 1")])
        # r.print_dropdown(dropdown, line_width=80)
        # assert r.n_lines == 3
        # assert r.line_number == 3
        #
        # r.move_cursor_to_line_editor(line_editor)
        # assert r.n_lines == 3
        # assert r.line_number == 0


        r = UIRender()
        line_editor = LineEditor()
        line_editor.enter_text("Hello")
        r.print_line_editor(line_editor)

        dropdown = Dropdown(items=[Item(title="item 1"), Item(title="item 2"), Item(title="item 3")])
        dropdown.press_down(1)
        r.print_dropdown(dropdown, line_width=80)
        assert r.n_lines == 7
        assert r.line_number == 7

        r.move_cursor_to_line_editor(line_editor)
        assert r.n_lines == 7
        assert r.line_number == 0


if __name__ == "__main__":
    from zelfred.tests import run_cov_test

    run_cov_test(__file__, "zelfred.render", preview=False)
