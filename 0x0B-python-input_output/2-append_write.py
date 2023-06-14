#!/usr/bin/python3

def append_write(filename="", text=""):
    text = text.replace("\n", " ")
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
        return len(text)
