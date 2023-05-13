# -*- coding: utf-8 -*-
import http.client
import urllib
import json
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'910fb0d8609eb9f3fcba574ecb0e0dd6'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/caihongpi/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
data = data["newslist"][0]["content"]  
data = data + "XXX"
a = len(data)
if(a > 20):
    data1 = data[0:19]
    data2 = data[20:-1]

data.replace("XXX","张存婷")
print(data)