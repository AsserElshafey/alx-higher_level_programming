#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ".?:"
    output = ""

    for char in text:
        output += char
        if char in punctuation:
            output += "\n\n"

    output = output.strip()
    print(output)
