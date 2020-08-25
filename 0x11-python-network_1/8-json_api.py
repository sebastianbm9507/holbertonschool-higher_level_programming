#!/usr/bin/python3
"""
Post to server
"""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        dict['q'] = argv[1]
    else:
        dict = {'q': ""}
    response = requests.post("http://0.0.0.0:5000/search_user", dict)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if response.json():
            print("[{}] {}".format(response.json().get('id'),
                  response.json().get('name')))
        else:
            print("No result")

