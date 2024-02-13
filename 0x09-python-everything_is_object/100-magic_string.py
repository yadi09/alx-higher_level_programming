#!/usr/bin/python3
def magic_string(dic={"count": 0}):
    dic["count"] += 1
    return str("BestSchool, " * dic["count"])[:-2]
