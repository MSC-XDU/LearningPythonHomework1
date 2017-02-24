# -*- coding:utf-8 -*-
__author__ = 'dlmyb'

import urllib2
import json

try:
    with open("token.json") as f:
        pass
    print "token.json already existed."
    exit(0)
except IOError:
    pass

email = raw_input("please input your email:")
j = {
    "email":email
}
req = urllib2.Request("http://xdmscpythonlearning.leanapp.cn", json.dumps(j),{'Content-Type':'application/json','Content-Length':str(len(json.dumps(j)))})
r = urllib2.urlopen(req)
token = r.read()
j['token'] = token

with open("token.json","w+") as f:
    f.write(json.dumps(j))

print '-'*30
print "Here's your account:"
print "email:{}".format(j['email'])
print "token:{}".format(j['token'])
print '-'*30
print "Please confirm your email address"
print "For further information,please read README."