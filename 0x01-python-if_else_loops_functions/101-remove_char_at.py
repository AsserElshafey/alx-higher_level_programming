#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    nstr = ""
    for i in range(len(str)):
        if i != n:
            nstr += str[i]
    return nstr
