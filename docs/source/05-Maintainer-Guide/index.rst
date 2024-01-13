Maintainer Guide
==============================================================================


Code Architecture Design
------------------------------------------------------------------------------


User Input Line Editor
------------------------------------------------------------------------------
:class:`LineEditor (zelfred.line_editor.LineEditor) <zelfred.line_editor.LineEditor>` 是一个单行用户输入文本框的实现. 它负责 UI app 的输入. 它本身不会 render UI, 它只是保存了 render 所需的全部数据. 这些数据包括:

1. 用户已经输入的文本.
2. 游标的位置.

并且这个类还实现了很多用于模拟人类的键盘动作的行为, 例如输入一个字符, 按一下退格键, 按一下左右键等. 人类按下按键后, 内存中的数据就要对应地发生变化. 所以我们把这些变化用人类可读的方法封装了起来, 这样能大幅增加代码可读性.


Dropdown Menu
------------------------------------------------------------------------------
:class:`Dropdown (zelfred.dropdown.Dropdown) <zelfred.dropdown.Dropdown>` 是一个下拉列表的实现. 用于展示 UI app 的输出. 下拉列表本质是一堆有序的 item, 这里我们不展开说 item. 它本身不会 render UI, 它只是保存了 render 所需的全部数据. 这些数据包括:

1. 所有的 item 的列表.
2. 当前选中的 item 的索引.
3. 当前游标, 也就是所选的 item 在 UI 中的索引. 因为 UI 不会展示所有的 item, 所以这个索引跟 #2 是不一样的.
4. 最多显示多少个 item 的常数.
5. 上下滚动时跳过多少个 item 的常数.

类似 ``LineEditor`` 这个类也实现了很多用于模拟人类的键盘动作的行为. 例如上下键选择 item, 上下滚动等等.


Item
------------------------------------------------------------------------------
:class:`Item (zelfred.item.Item) <zelfred.item.Item>` 是 ``Dropdown`` 中所展示的内容. 对于人类可见的部分有 title 和 subtitle, 以及是否被选中的状态. 对于人类不可见的有它的 arg (argument) 以及一个 variables 字典数据结构, 以及一些定义了当用户按下某些快捷键时 (例如 Enter, Ctrl + A) 所执行的动作. 可以说 Item 是用户交互中最重要的部分. 它用视觉化的方式展示了输出数据, 并且定义了交互行为.

你可以通过继承这个类并实现这些方法来自定义用户和 item 交互的行为:

- :meth:`~.zelfred.item.Item.enter_handler`
- :meth:`~.zelfred.item.Item.post_enter_handler`
- :meth:`~.zelfred.item.Item.ctrl_a_handler`
- :meth:`~.zelfred.item.Item.post_ctrl_a_handler`
- :meth:`~.zelfred.item.Item.ctrl_w_handler`
- :meth:`~.zelfred.item.Item.post_ctrl_w_handler`
- :meth:`~.zelfred.item.Item.ctrl_u_handler`
- :meth:`~.zelfred.item.Item.post_ctrl_u_handler`
- :meth:`~.zelfred.item.Item.ctrl_p_handler`
- :meth:`~.zelfred.item.Item.post_ctrl_p_handler`


Render Engine
------------------------------------------------------------------------------
:class:`Render (zelfred.render.Render) <zelfred.render.Render>` 是一个以行为单位的渲染引擎, 它能控制将字符串流打印到终端上, 并且对游标的位置进行管理. 而 :class:`UIRender (zelfred.render.UIRender) <zelfred.render.UIRender>` 则是继承了 ``Render`` 并且为 zelfred UI 的交互逻辑做了很多优化, 方便开发者对其进行编程.

``UIRender`` 有这些跟 UI 交互逻辑相关的方法:

- :meth:`~zelfred.render.UIRender.print_line_editor`
- :meth:`~zelfred.render.UIRender.clear_line_editor`
- :meth:`~zelfred.render.UIRender.update_line_editor`
- :meth:`~zelfred.render.UIRender.process_title`
- :meth:`~zelfred.render.UIRender.process_subtitle`
- :meth:`~zelfred.render.UIRender.print_item`
- :meth:`~zelfred.render.UIRender.print_dropdown`
- :meth:`~zelfred.render.UIRender.clear_dropdown`
- :meth:`~zelfred.render.UIRender.update_dropdown`
- :meth:`~zelfred.render.UIRender.move_cursor_to_line_editor`
- :meth:`~zelfred.render.UIRender.print_ui`
- :meth:`~zelfred.render.UIRender.move_to_end`
- :meth:`~zelfred.render.UIRender.clear_ui`


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
当你按下 F1 按键时, 会调用 :meth:`UIProcessKeyPressedMixin.process_f1 <zelfred.ui_process_key_pressed.UIProcessKeyPressedMixin.process_f1>` 方法, 通过读源码可以看到它其实是 raise 了一个 :class:`~zelfred.exc.JumpOutSessionError`. 而抛异常这个动作其实还是在 :meth:`UI.run_session <zelfred.ui.UI.run_session>` 中的 ``main_loop()`` 中的. 通过读源码可以看到这个异常会被 ``try ... except ...`` 捕获, 并调用 :meth:`UI.jump_out_session_loop <zelfred.ui.UI.jump_out_session_loop>` 来处理. 通过读源码可以看到这个处理逻辑本质上是恢复了之前的 handler, 并且立刻用它来处理之前的 input query, 然后重新 render UI, 并且回到 :meth:`UI.run_session <zelfred.ui.UI.run_session>` 的逻辑中, 用 ``self.run_session(_do_init=False)`` 进入了一个新的 session. 由于 session 的本质是 handler, 它只是在内存中不是一个对象了, 但逻辑上跟你之前的 parent session 是一模一样的.
