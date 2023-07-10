#!/usr/bin/python3
"""
Contains the inherits_from function

"""


def inherits_from(obj, a_class):

    obj_type = type(obj)
    is_class = issubclass(obj_type, a_class) and obj_type is not a_class
    return is_class
