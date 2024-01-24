#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = [x if x != search else replace for x in my_list]
    return new_list
