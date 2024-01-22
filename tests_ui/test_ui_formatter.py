# -*- coding: utf-8 -*-

import os
import pytest

from zelfred.ui import UI


class TestUIFormatterMixin:
    def test(self):
        ui = UI(handler=lambda x: [])
        print(ui.TAB)
        print(ui.ENTER)
        print(ui.CTRL_A)
        print(ui.CTRL_W)
        print(ui.CTRL_U)
        print(ui.CTRL_P)
        print(ui.F1)
        print(ui.CTRL_T)
        print(ui.CTRL_G)
        print(ui.CTRL_B)
        print(ui.CTRL_N)
        print("my name is {}".format(ui.format_highlight("Alice")))
        print(ui.format_key_value("key", "value"))


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    pytest.main([abspath, "-s", "--tb=native"])
