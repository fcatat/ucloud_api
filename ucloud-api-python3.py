# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     ucloudAPI
   Description :  按照下列方式运行，需要实现的功能查询ucloudAPI页面
   python ucloud-api-python3.py DescribeURedisGroup.yml 

-------------------------------------------------
   Change Activity:2018/12/24
   Change Activity:2019/03/27
   Author:            jixing
---
-------------------------------------------------
"""
# 功能与2.0脚本一致，目前测试版本3.6.6
import hashlib
from urllib import parse
import urllib
import yaml
import sys
import requests


filename = sys.argv[1]
conf = open(filename)
conf = yaml.load(conf)

api = 'https://api.ucloud.cn'

public_key = "改为自己的"
private_key = "改为自己的"


url_par = conf[0]['url_par']
url_par['PublicKey'] = public_key
items = url_par.items()
items = sorted(items)

params_data = ''
for key, value in items:
    params_data += str(key) + str(value)
params_data += private_key

sign = hashlib.sha1()
sign.update(params_data.encode("utf8"))
signature = sign.hexdigest()

url_par['Signature'] = signature
url_params = urllib.parse.urlencode(url_par)

res = requests.get(api, params=url_params)
print(res.text)
