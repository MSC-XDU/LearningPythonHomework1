# -*- coding:utf-8 -*-
__author__ = 'dlmyb'

import json

def writeToken():
    account = raw_input('input your email:')
    token = raw_input('input your token:')
    j = {'account': account, 'token': token}
    with open('token.json', 'w+') as f:
        f.write(json.dumps(j))
    return account, token

try:
    with open('token.json','r') as f:
        j = json.loads(f.read())
    account = j['account']
    token = j['token']
    if "N" == raw_input("""keep using {} account? (Y/N):""".format(account)):
        raise KeyError
except IOError:
    account, token = writeToken()
except KeyError:
    account, token = writeToken()

print '-'*30

from lib.checkSolution import upload
upload(account, token)