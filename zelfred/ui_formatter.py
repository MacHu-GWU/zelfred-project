# -*- coding: utf-8 -*-

"""
See :class:`UIFormatterMixin`.
"""

import typing as T

if T.TYPE_CHECKING:
    from .ui import UI


class UIFormatterMixin:
    """
    This mixin class implements helper functions to format terminal output.
    """

    def format_shortcut(self: "UI", key: str) -> str:
        """
        Format a keyboard shortcut key. By default, the color is magenta.
        Example:

            :magenta:`Enter` to open url
        """
        return f"{self.terminal.magenta}{key}{self.terminal.normal}"

    @property
    def TAB(self) -> str:
        return self.format_shortcut("Tab")

    @property
    def ENTER(self) -> str:
        return self.format_shortcut("Enter")

    @property
    def CTRL_A(self) -> str:
        return self.format_shortcut("Ctrl A")

    @property
    def CTRL_W(self) -> str:
        return self.format_shortcut("Ctrl W")

    @property
    def CTRL_U(self) -> str:
        return self.format_shortcut("Ctrl U")

    @property
    def CTRL_P(self) -> str:
        return self.format_shortcut("Ctrl P")

    @property
    def F1(self) -> str:
        return self.format_shortcut("F1")

    @property
    def CTRL_T(self) -> str:
        return self.format_shortcut("Ctrl T")

    @property
    def CTRL_G(self) -> str:
        return self.format_shortcut("Ctrl G")

    @property
    def CTRL_B(self) -> str:
        return self.format_shortcut("Ctrl B")

    @property
    def CTRL_N(self) -> str:
        return self.format_shortcut("Ctrl N")

    def format_highlight(self: "UI", text: str) -> str:
        """
        Highlight a text with terminal color. In this project, the color is cyan.
        Example:

            this is a very :cyan:`Important message`!
        """
        return f"{self.terminal.cyan}{text}{self.terminal.normal}"

    def format_key(self: "UI", key: str) -> str:
        """
        Format a key of key-value-pair text with terminal color. In this project,
        the color is cyan. Example:

            tag :cyan:`environment` = :yellow:`production`
        """
        return self.format_highlight(key)

    def format_value(self: "UI", value: str) -> str:
        """
        Format a value of key-value-pair text with terminal color. In this project,
        the color is yellow. Example:

            tag :cyan:`environment` = :yellow:`production`
        """
        return f"{self.terminal.yellow}{value}{self.terminal.normal}"

    def format_key_value(self: "UI", key: str, value: T.Any) -> str:
        """
        Format a key-value pair text with terminal color. In this project, key is
        in cyan and value is in yellow. Example:

            tag :cyan:`environment` = :yellow:`production`
        """
        return f"{self.format_key(key)} = {self.format_value(value)}"
