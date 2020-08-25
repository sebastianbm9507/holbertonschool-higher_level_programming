#!/usr/bin/python3
"""  Write a Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests
    url = 'https://intranet.hbtn.io/status'
    result_request = requests.get(url)
    cont = result_request.text
    print('Body response:\n\t- type: {}\n\t- content: {}\
'.format(type(cont), cont))
