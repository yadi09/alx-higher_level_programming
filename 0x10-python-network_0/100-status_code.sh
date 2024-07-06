#!/bin/bash
# Bash script that sends a request to a URL passed as an argument,
curl -so /dev/null --write-out "%{http_code}" "$1"
