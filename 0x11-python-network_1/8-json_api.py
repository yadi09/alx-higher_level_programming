#!/usr/bin/python3
"""script"""
from sys import argv
import requests

if __name__ == "__main__":
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    respost = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_data = rspost.json()
        if json_data == {}:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
