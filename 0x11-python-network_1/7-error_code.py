#!/usr/bin/python3


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    result = requests.get(url)
    if result.status_code >= 400:
        print('Error code: {}'.format(result.status_code))
    else:
        print(result)
