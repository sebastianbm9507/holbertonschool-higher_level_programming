#!/usr/bin/python3
"""
Post to server
"""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        dic = {'q': argv[1]}
    else:
        dic = {'q': ""}
        url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, dic)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if response.json():
            print("[{}] {}".format(response.json().get('id'),
                  response.json().get('name')))
        else:
            print("No result")
