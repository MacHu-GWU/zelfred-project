.. _ui-event-loop:

UI Event Loop
==============================================================================
The UI is just an event loop. Firstly, it goes through the **initialization phase**, then enters the **main event loop**, processing user input and rendering the interactive UI. If it raises any errors and ``capture_error`` is set to ``True``, it will enter the **debug loop** and wait for the user to correct the input. Afterward, it returns to the main event loop.

**Initialization phase**: When the app is launched for the first time, it displays the line editor and some "hello" items. Then it runs the handler function to retrieve the items and update the dropdown menu.

**Main event loop**: It processes user input and then renders the UI.

**Debug loop**: It creates a debug item and renders the UI, then returns to the main event loop, waiting for user input."


Flow Chart
------------------------------------------------------------------------------
The flow chart below shows the UI event loop.

.. raw:: html
    :file: ./ui-event-loop.drawio.html


Print Query
------------------------------------------------------------------------------
Print the ``(Query): {user_query}`` line

Before (nothing in the terminal)::

    # NOTHING HERE

After. The ``beau`` is the user input query::

    (Query): beau


Run Handler
------------------------------------------------------------------------------
Run the handler function.


Print Items
------------------------------------------------------------------------------
Print items in the dropdown menu.

Before::

    (Query): beau

After::

    (Query): beau
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com


Move to the End
------------------------------------------------------------------------------
Move the cursor to the next line of the end of the dropdown menu.

Before, ``|`` is the cursor in the user input dialog::

    (Query): beau|
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com

After, the cursor is at begin of the line below the last item::

    (Query): beau
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com
    |


Clear Items
------------------------------------------------------------------------------
Clear the item dropdown menu.

Before::

    (Query): beau
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com
    |

After::

    (Query): beau
    |


Clear Query
------------------------------------------------------------------------------
Clear the ``(Query): {user_query}`` line.

Before::

    (Query): beau|
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com


After::

    |
    [x] Beautiful is better than ugly.
          subtitle 01: https://www.google.com
    [ ] Explicit is better than implicit.
          subtitle 02: https://www.google.com
    [ ] Simple is better than complex.
          subtitle 03: https://www.google.com
    [ ] Complex is better than complicated.
          subtitle 04: https://www.google.com
    [ ] Flat is better than nested.
          subtitle 05: https://www.google.com


Process Input
------------------------------------------------------------------------------
Process the keyboard event, update the :class:`~zelfred.line_editor.LineEditor` and :class:`~zelfred.dropdown.Dropdown` objects. So the following ``print_query`` and ``print_items`` can render the UI correctly.
