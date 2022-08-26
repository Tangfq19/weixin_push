# -*- coding: utf-8 -*-
import http.client, urllib
import json
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'910fb0d8609eb9f3fcba574ecb0e0dd6'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/lzmy/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
print(data["newslist"][0]["saying"])