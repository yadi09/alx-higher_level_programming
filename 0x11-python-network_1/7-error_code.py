#!/usr/bin/python3
"""script that takes in a URL
sends a request to the URL and
displays the body of the response."""
import requests
import sys

if __name__ == "__main__":
    respo = requests.get(sys.argv[1])
    status_code = respo.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(respo.text)
