.. _app-gallery:

App Gallery
==============================================================================
https://asciinema.org/a/617868


Random Password Generator
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

The user enters the length of the password, and the UI generates a few random passwords for the user to choose from. The user can tap "Enter" to copy the selected password to the clipboard.

**Demo**

.. image:: https://asciinema.org/a/617869.svg
    :target: https://asciinema.org/a/617869

**Source Code**

.. literalinclude:: ./e01_random_password_generator.py
   :language: python
   :linenos:


Calculate File Checksum
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

The user enters (or paste) the absolute path of the file, and the UI generates a few checksum algorithm options, then user can choose one and hit "Enter" to copy the checksum value of the selected algorithm. The UI will stay and user can continue to choose another algorithm and hit "Enter" again.

**Demo**

.. image:: https://asciinema.org/a/617871.svg
    :target: https://asciinema.org/a/617871

**Source Code**

.. literalinclude:: ./e02_calculate_file_checksum.py
   :language: python
   :linenos:


Select Item Using Fuzzy Match
------------------------------------------------------------------------------
:bdg-success:`Difficulty: Easy`

Use the user input to sort a list of items by fuzzy match similarity. Allow user to tap "Enter" to copy the content to clipboard.

**Demo**

.. image:: https://asciinema.org/a/617874.svg
    :target: https://asciinema.org/a/617874

**Source Code**

.. literalinclude:: ./e03_select_item_using_fuzzy_match.py
   :language: python
   :linenos:


Google Search with Suggestion
------------------------------------------------------------------------------
:bdg-warning:`Difficulty: Medium`

User type query and return a dropdown list of suggestions. User can tab "Enter" to Google search in web browser.

**Demo**

.. image:: https://asciinema.org/a/616014.svg
    :target: https://asciinema.org/a/616014

**Source Code**

.. literalinclude:: ./e02_google_search_with_suggestion.py
   :language: python
   :linenos:


Folder and File Search
------------------------------------------------------------------------------
:bdg-danger:`Difficulty: Hard`

User can search folder in a root directory, and then tab "Enter" to enter a sub query session to search file in the selected folder. At the end, user can tab "Enter" to open the file using the default application.

**Demo**

.. image:: https://asciinema.org/a/616119.svg
    :target: https://asciinema.org/a/616119

**Source Code**

.. literalinclude:: ./e03_folder_and_file_search.py
   :language: python
   :linenos:


Search Google Chrome Bookmark
------------------------------------------------------------------------------
:bdg-danger:`Difficulty: Hard`

User type query and return a dropdown list of matched Google Chrome bookmarks. User can tap "Enter" to open it in default web browser.

**Demo**

.. image:: https://asciinema.org/a/617801.svg
    :target: https://asciinema.org/a/617801

**Source Code**

.. literalinclude:: ./e04_search_google_chrome_bookmark.py
   :language: python
   :linenos:


Password Book App
------------------------------------------------------------------------------
:bdg-danger:`Difficulty: Hard`

User the user input to search the username, allow user to tap "Ctrl A" to copy the password to clipboard. Afterward, the UI doesn't exit and wait for the next user input.

**Demo**

.. image:: https://asciinema.org/a/617807.svg
    :target: https://asciinema.org/a/617807

**Source Code**

.. literalinclude:: ./e05_password_book.py
   :language: python
   :linenos:
