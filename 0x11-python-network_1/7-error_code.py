#!/usr/bin/python3
""" sends a request to the URL and
    displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    try:
        result = requests.get(url)
        print(result.text)
    except Exception as error:
        print('Error code: {}'.format(error.status_code))
