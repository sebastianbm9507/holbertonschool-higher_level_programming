#!/usr/bin/python3
"""  sends a POST request to the passed URL with the email as a
    parameter, and displays the body of the response (decoded in utf-8)
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('UTF-8'))
