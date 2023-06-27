#!/usr/bin/python3
"""Module presents function that inserts indentation."""

def text_indentation(text):
    """Inserts text indentation.

    Args:
        text - string to be indented.

    Returns:
        no return value

    Raises:
        TypeError: if text is not string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in range(len(text)):
        if (text[i] == 46 or text[i] == 63 or text[i] == 58):
            text =+ 1
            print(text, end='\n')
