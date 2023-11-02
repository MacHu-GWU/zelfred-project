# -*- coding: utf-8 -*-

"""
本例详细的研究了 ``readchar.readkey()`` 在读用户的输入时的系统行为.

当 ``readchar.readkey()`` 被调用时, Python 将会进入等待. 如果用户输入的是
"""

import readchar


def example1():
    """
    当用户按下 CTRL C 时候, 下面的 ``if key == readchar.key.CTRL_C`` 压根没有被执行,
    直接就在 ``key = readchar.readkey()`` 哪一行抛出了 ``KeyboardInterrupt`` 异常.
    所以你不会见到 ``KeyboardInterrupt("user entered CTRL C!")`` 的信息
    """
    while 1:
        key = readchar.readkey()
        print([key])
        if key == readchar.key.CTRL_C:
            raise KeyboardInterrupt("user entered CTRL C!")


def example2():
    """
    如果我们要对 KeyboardInterrupt 进行处理, 就必须将 ``key = readchar.readkey()``
    用 ``try ... except ...`` 包围起来, 然后在 ``except`` 里面处理 ``KeyboardInterrupt``.
    这里我们选择继续抛出这个异常中断程序. 而如果我们直接 pass, 由于我们有 ``while 1`` 的
    存在, 那么我们将无法用 ``CTRL C`` 来中断程序.
    """
    while 1:
        try:
            key = readchar.readkey()
            print([key])
        except KeyboardInterrupt:
            print("enter 'except KeyboardInterrupt' statement")
            raise KeyboardInterrupt("user entered CTRL C!")


if __name__ == "__main__":
    # example1()
    example2()
    pass
