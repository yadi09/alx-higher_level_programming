#!/usr/bin/python3
"""script that takes in a URL and an email address
sends a POST request to the passed URL
with the email as a parameter"""
import requests
import sys

if __name__ == "__main__":
    respo = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(respo.text)
