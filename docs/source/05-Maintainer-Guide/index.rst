Maintainer Guide
==============================================================================




Code Architecture Design
------------------------------------------------------------------------------


User Input Line Editor
------------------------------------------------------------------------------
:class:`LineEditor (zelfred.line_editor.LineEditor) <zelfred.line_editor.LineEditor>`


Dropdown Menu
------------------------------------------------------------------------------
:class:`Dropdown (zelfred.dropdown.Dropdown) <zelfred.dropdown.Dropdown>`


Item
------------------------------------------------------------------------------
:class:`Item (zelfred.item.Item) <zelfred.item.Item>`


Render Engine
------------------------------------------------------------------------------
:class:`Render (zelfred.render.Render) <zelfred.render.UIRender>`, :class:`UIRender (zelfred.render.UIRender) <zelfred.render.UIRender>`


Keystroke Event
------------------------------------------------------------------------------
:meth:`UI.main_loop <zelfred.ui.UI.main_loop>`, :meth:`UI.process_input <zelfred.ui.UI.process_input>`, :meth:`UI.process_input <zelfred.ui.UI.process_key_pressed_input>`



Shortcut Key
------------------------------------------------------------------------------


如何实现选中 Item 按下 Item Action 快键键后不退出 App
------------------------------------------------------------------------------
当你按下任何跟 Item Action 相关的快捷键 (例如 Enter, Ctrl + A 等等), 会调用相关的方法, 例如 :meth:`~zelfred.ui_process_key_pressed.UIProcessKeyPressedMixin.process_enter` 这个. 而观察这个方法会依次运行 :meth:`Item.enter_handler <zelfred.item.Item.enter_handler>` 和 :meth:`Item.enter_handler <zelfred.item.Item.post_enter_handler>` 方法. 默认情况下 ``post_enter_handler`` 会抛出 ``EndOfInputError`` 异常. 如果你要将其设为按下 Item Action 快捷键后不退出, 你在你的自定义 handler 返回的 item 类中 override ``post_enter_handler`` 方法, 把它设为 ``pass``, 什么都不做即可.


如何实现按进入 sub session
------------------------------------------------------------------------------
启动 UI 后会依次运行以下方法 :meth:`UI.run <zelfred.ui.UI.run>` -> :meth:`UI.run_session <zelfred.ui.UI.run_session>` -> (:meth:`UI.initialize_loop <zelfred.ui.UI.initialize_loop>` -> :meth:`UI.main_loop <zelfred.ui.UI.main_loop>` -> :meth:`UI.debug_loop <zelfred.ui.UI.debug_loop>`).

其中 :meth:`UI.main_loop <zelfred.ui.UI.main_loop>` 这个函数在大多数情况下是用户在输入框每按下一次就走一遍循环. 其中第一步 :meth:`UI.process_input <zelfred.ui.UI.process_input>` 函数会处理用户的键盘输入. 这个函数在底层根据输入的 key 然后到这个 :class:`~zelfred.ui_process_key_pressed.UIProcessKeyPressedMixin` 类里去找对应的函数. 这个函数一般是根据选定的 :class:`~zelfred.item.Item`, 去运行 item 中的 user defined item action 方法. 例如 :meth:`Item.enter_handler <zelfred.item.Item.enter_handler>`, :meth:`Item.ctrl_a_handler <zelfred.item.Item.ctrl_a_handler>` 等. 这些方法里你就可以做任何事情, 例如打开浏览器, 复制到剪贴板, 打开文件等. 我们拿 :meth:`~zelfred.ui_process_key_pressed.UIProcessKeyPressedMixin.process_enter` 的源码为例看, 它的默认行为会找到 selected item 并运行 :meth:`Item.enter_handler <zelfred.item.Item.enter_handler>` 方法.

所以进入 sub session 的关键是修改 ``Item.enter_handler`` 方法. 这里我们有一个例子 :ref:`app-gallery-folder-and-file-search`. 请仔细阅读 ``FolderItem.enter_handler`` 中的注释理解我们如何创建一个为 sub session 服务的 handler 函数, 以及如何进入 sub session 并设定初始的 query input.


如何实现按快捷键跳出 Sub Session
------------------------------------------------------------------------------
:meth:`UIProcessKeyPressedMixin.process_f1 <zelfred.ui_process_key_pressed.UIProcessKeyPressedMixin.process_f1>`

:class:`~zelfred.exc.JumpOutSessionError`

