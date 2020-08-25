#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
        url = 'http://0.0.0.0:5000/search_user'
    # POST REQUEST
    result = requests.post(url, values)
    if result.headers.get('content-type') == 'application/json':
        if not result.json():
            print("No result")
        else:
            print("[{}] {}\
".format(result.json()['id'], result.json()['name']))
    else:
        print("Not a valid JSON")
