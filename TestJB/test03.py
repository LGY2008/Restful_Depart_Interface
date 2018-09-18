#encoding=utf-8
import json

import requests
# 查询所有学院
url="http://127.0.0.1:8000/api/departments/"
# 调用GET请求
# response=requests.get(url)
# 以text形式获取结果
# result=response.json()
# print(result)
# code=response.status_code
# print(code)
# response.raise_for_status()
# print(response.content)
# print(response.url)
# print(response.apparent_encoding)
# print(response.headers)
# flag= response.status_code == requests.codes.ok
# print(flag)
# params={"$dep_id_list":"T01"}
params={"$dep_id_list":"T01,T03"}
r=requests.get(url,params=params)
print(r.content)
# r.encoding='utf-8'
print(r.encoding)
print(r.json())
print(r.url)