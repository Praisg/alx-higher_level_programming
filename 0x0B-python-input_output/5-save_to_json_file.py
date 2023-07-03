#!/usr/bin/python3

"""Define json module """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an txt file.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
