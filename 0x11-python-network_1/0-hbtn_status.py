#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    data_decode = data.decode('UTF-8')
    print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}\
'.format(type(data), data, data_decode))
