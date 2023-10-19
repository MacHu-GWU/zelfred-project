# -*- coding: utf-8 -*-

from zelfred.item import T_ITEM, Item



def test():
    print("")
    _test_press_key()
    _test_enter_text()
    _test_press_backspace()
    _test_press_left()
    _test_press_home()
    _test_press_delete()
    _test_press_right()
    _test_press_end()
    _test_clear_line()
    _test_clear_backward()
    _test_clear_forward()
    _test_move_word()


if __name__ == "__main__":
    from zelfred.tests import run_cov_test

    run_cov_test(__file__, "zelfred.line_editor", preview=False)
