Test for 5-text_indentation module
===================================

This module defines a text-formatting function ``text_indentation(text)``.

Usage
-----

``text_indentation()`` prints text with 2 new lines after each '.', '?', and ':'.

    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("Hello?")
    Hello?
    <BLANKLINE>

    >>> text_indentation("Hello.World")
    Hello.
    <BLANKLINE>
    World

    >>> text_indentation("Hello:World?How are you.")
    Hello:
    <BLANKLINE>
    World?
    <BLANKLINE>
    How are you.
    <BLANKLINE>

No spaces at beginning or end of lines:

    >>> text_indentation("   Hi there.")
    Hi there.
    <BLANKLINE>

    >>> text_indentation("Let's print a long text with some special characters:     and this can be annoying but it should work with any type of characters?")
    Let's print a long text with some special characters:
    <BLANKLINE>
    and this can be annoying but it should work with any type of characters?
    <BLANKLINE>

Empty string:

    >>> text_indentation("")

Invalid Text
------------

The parameter ``text`` must be a string:

    >>> text_indentation(7)
    Traceback (most recent call last):
    TypeError: text must be a string

    >>> text_indentation(None)
    Traceback (most recent call last):
    TypeError: text must be a string

Missing Arguments
-----------------

One argument is required:

    >>> text_indentation()
    Traceback (most recent call last):
    TypeError: text_indentation() missing 1 required positional argument: 'text'

Test for 6-max_integer module
=============================

This module defines a function ``max_integer(list)``.

Usage
-----

``max_integer()`` returns the maximum integer in a list.

    >>> max_integer = __import__('6-max_integer').max_integer
    >>> max_integer([1, 2, 3, 4])
    4

    >>> max_integer([1, 3, 4, 2])
    4

Empty list:

    >>> max_integer([])

Single element:

    >>> max_integer([1])
    1

Negative numbers:

    >>> max_integer([-1, -2, -3])
    -1

Mixed positive and negative:

    >>> max_integer([-1, 2, -3, 4])
    4