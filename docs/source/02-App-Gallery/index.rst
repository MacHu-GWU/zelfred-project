.. _app-gallery:

App Gallery
==============================================================================


Random Password Generator
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

The user enters the length of the password, and the UI generates a few random passwords for the user to choose from. The user can tap "Enter" to copy the selected password to the clipboard.

**Demo**

.. image:: https://asciinema.org/a/617869.svg
    :target: https://asciinema.org/a/617869

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e01_random_password_generator.py
       :language: python
       :linenos:


Calculate File Checksum
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

The user enters (or paste) the absolute path of the file, and the UI generates a few checksum algorithm options, then user can choose one and hit "Enter" to copy the checksum value of the selected algorithm. The UI will stay and user can continue to choose another algorithm and hit "Enter" again.

**Demo**

.. image:: https://asciinema.org/a/617871.svg
    :target: https://asciinema.org/a/617871

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e02_calculate_file_checksum.py
       :language: python
       :linenos:


Select Item Using Fuzzy Match
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

Use the user input to sort a list of items by fuzzy match similarity. Allow user to tap "Enter" to copy the content to clipboard.

**Demo**

.. image:: https://asciinema.org/a/617874.svg
    :target: https://asciinema.org/a/617874

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e03_select_item_using_fuzzy_match.py
       :language: python
       :linenos:


Google Search with Suggestion
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

The user types a query and receives a dropdown list of Google search suggestions. The user can then tap "Enter" to perform a Google search in their web browser.

**Demo**

.. image:: https://asciinema.org/a/616014.svg
    :target: https://asciinema.org/a/616014

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e04_google_search_with_suggestion.py
       :language: python
       :linenos:


Search Google Chrome Bookmark
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

User type query and return a dropdown list of matched Google Chrome bookmarks. User can tap "Enter" to open it in default web browser.

**Demo**

.. image:: https://asciinema.org/a/617801.svg
    :target: https://asciinema.org/a/617801

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e05_search_google_chrome_bookmark.py
       :language: python
       :linenos:


.. _app-gallery-folder-and-file-search:

Folder and File Search
------------------------------------------------------------------------------
:bdg-danger:`Difficulty: Hard`

User can search folder in a root directory, and then tap "Enter" to enter a sub query session to search file in the selected folder. At the end, user can tab "Enter" to open the file using the default application. Also, user can tap "F1" to exit the sub query session and go back to the folder search session.

**Demo**

.. image:: https://asciinema.org/a/616119.svg
    :target: https://asciinema.org/a/616119

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e06_folder_and_file_search.py
       :language: python
       :linenos:


Password Book App
------------------------------------------------------------------------------
:bdg-danger:`Difficulty: Hard`

User the user input to search the username, allow user to tap "Ctrl A" to copy the password to clipboard. Afterward, the UI doesn't exit and wait for the next user input.

**Demo**

.. image:: https://asciinema.org/a/617807.svg
    :target: https://asciinema.org/a/617807

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e05_password_book.py
       :language: python
       :linenos:


Refresh Cache V1
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

No matter what user entered, always return a random value between 1 and 100. And this value is based on cache that won't change while user is typing. However, we want to provide a way to refresh the value. User can type "!~" and then hit "ENTER" to refresh the value. When user hit ENTER, it automatically removes the "!~" part and recover the original query.

**Demo**

.. image:: https://asciinema.org/a/631197.svg
    :target: https://asciinema.org/a/631197

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e08_refresh_cache_v1.py
       :language: python
       :linenos:


Refresh Cache V2
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

No matter what user entered, always return a random value between 1 and 100. And this value is based on cache that won't change while user is typing. However, we want to provide a way to refresh the value. User can type "!~", then the value will be immediately refreshed, and the "!~" will be removed automatically.

**Demo**

.. image:: https://asciinema.org/a/631325.svg
    :target: https://asciinema.org/a/631325

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e09_refresh_cache_v2.py
       :language: python
       :linenos:


Refresh Cache V3
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

No matter what user entered, always return a random value between 1 and 100. And this value is based on cache that won't change while user is typing. However, we want to provide a way to refresh the value. User can type "!~", then the value will be refreshed after 1 seconds, and the "!~" will be removed automatically. During the waiting, it will show a helper text to tell user to wait.

**Demo**

.. image:: https://asciinema.org/a/631335.svg
    :target: https://asciinema.org/a/631335

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e10_refresh_cache_v3.py
       :language: python
       :linenos:


JSON Formatter
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

Copy JSON text to clipboard, then hit 'Enter' to dump the formatted JSON to
``${HOME}/tmp/formatted.json`` and automatically open it.

**Demo**

.. dropdown:: **Source Code**

    .. literalinclude:: ../../../zelfred/gallery/./e11_json_formatter.py
       :language: python
       :linenos:
