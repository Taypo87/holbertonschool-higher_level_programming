#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

    print('Body response:$')
    print('\t- type: <{}>'.format(type(response)))
    print('\t- content: {}'.format(response))
    print('\t- utf8 content: {}'.format(content.decode('utf-8')))
