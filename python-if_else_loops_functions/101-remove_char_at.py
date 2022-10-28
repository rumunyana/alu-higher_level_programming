#!/usr/bin/python3
def remove_char_at(str, n):
    position = 0
    new = ""
    for char in str:
        if position != n:
            new += char
        position += 1
    return (new)
