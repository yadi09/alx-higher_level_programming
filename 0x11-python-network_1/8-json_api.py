#!/usr/bin/python3
"""script"""
import requests
import sys

if __name__ == "__main__":
    str = {"q": sys.argv[1][0] if len(sys.argv) > 1 else ""}
    rspo = requests.post("http://0.0.0.0:5000/search_user", data=str)
    try:
        json = rspo.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
