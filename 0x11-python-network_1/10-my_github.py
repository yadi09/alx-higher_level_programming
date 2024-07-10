#!/usr/bin/python3
"comment"

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
