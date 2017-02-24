# -*- coding:utf-8 -*-
__author__ = 'dlmyb'

import traceback
from exceptions import Exception
import inspect
try:
    import cPickle as pickle
except:
    import pickle

import urllib2, json

def upload(email,token):
    with open('solution.py','r') as f:
        code = f.read()
    j = {
        "email":email,
        "password":token,
        "result":json.dumps(final),
        "quizName":CONFIG['quizName'],
        'code':code
    }
    req = urllib2.Request("http://xdmscpythonlearning.leanapp.cn/submit", json.dumps(j),{'Content-Type':'application/json','Content-Length':str(len(json.dumps(j)))})
    f = urllib2.urlopen(req)
    print f.read()
    f.close()


class resultException(Exception):
    def __init__(self,dataset,result):
        self.dataset = dataset
        self.result = result

dataset = pickle.load(open("rawdata.bin","rb")) # 挂载测试数据集

try:
    import solution
    s = solution.Solution() # 能否编译通过
except:
    print traceback.print_exc()
    exit(0)

with open("config.json","r") as f:
    CONFIG = json.loads(f.read())

funcMember = dict(inspect.getmembers(s))
funcList = list()

for funcName in CONFIG["function"]:
    try:
        funcList.append(funcMember[funcName])
    except KeyError:
        print u"请检查 solotion.py 格式是否正确"
        exit(0)

final = {i.__name__: False for i in funcList}

for func in funcList:
    flag = 1
    for data in dataset[func.__name__]:
        try:
            result = func(**data['input']) # 验证结果
            if result == None:
                flag = 2
                continue
            if data['result'] != result:
                raise resultException(data, result)
        except resultException as e:
            print u"在 {} 函数中,出现错误答案:".format(func.__name__)
            print u"input:{} \noutput:{}\ncurrent:{}".format(
                data['input'], func(**data['input']), data['result']
            )
            # final[func.__name__] = False
            flag = 0
            break
        except:
            traceback.print_exc()
            flag = 2
    if flag == 1:
        print u"{} 函数测试通过".format(func.__name__)
        final[func.__name__] = True
    elif flag == 2:
        print u"{} 函数未完成".format(func.__name__)
    print '-'*30




