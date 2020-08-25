#!/usr/bin/python3
""" Sends a request to the URL and displays the value
    of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    result_request = requests.get(url)
    header_id = result_request.headers.get('X-Request-Id')
    print(header_id)
