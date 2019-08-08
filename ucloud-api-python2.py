#!/usr/bin/python
# -*- coding: UTF8 -*-
"""
-------------------------------------------------
   File Name：     ucloudAPI
   Description : 

-------------------------------------------------
   Change Activity:2019/03/27
   Author:            jixing
---
-------------------------------------------------
"""
# 版本2.7
import yaml;
import hashlib;
import urllib;
import requests;
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

#读取配置文件
filename=sys.argv[1]
conf = open(filename);
conf = yaml.load(conf);

#api
api = 'https://api.ucloud.cn';

#获取公钥和密钥
#key = conf[1]['keys'];
public_key = "改为自己的"
private_key = "改为自己的"
#拼接URL参数
url_par = conf[0]['url_par'];

url_par['PublicKey'] = public_key;
items = url_par.items();
#参数排序
items.sort();

params_data = '';
for key, value in items:
  params_data += str(key) + str(value);

params_data += private_key;
#计算签名
sign = hashlib.sha1();
sign.update(params_data);
signature = sign.hexdigest();
#对URL字符型进行编码
url_par['Signature'] = signature;
url_params = urllib.urlencode(url_par);

#请求URL
res = requests.get(api, params = url_params);
print res.text;
