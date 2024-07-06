#!/bin/bash
# script a JSON POST
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
