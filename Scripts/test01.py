import json

import requests
# 查询学院所有
# str=requests.get('http://127.0.0.1:8000/api/departments/')
# # 断言状态码是否为200
# print("获取状态码：",str.status_code)
# print("获取的json值为：",str.json())

# 查询学院指定

# str=requests.get(url='http://127.0.0.1:8000/api/departments/T03/')
#
# print(str.status_code)
# print(str.url)

# dec={'dep_id': 'T03', 'dep_name': 'C++学院', 'master_name': 'C++-Master', 'slogan': 'Here is Slogan'}
# dec={'dep_id': 'T03'}
# dec="T03"
# str=str.json()
# dec=json.dumps(dec)
# print("类型为：",type(str))
# print(str)
# try:
#     assert dec == str
#     print("断言成功，相等")
# except:
#     print("断言失败，不相等")


# 查询学院 list
# str=requests.get(url='http://127.0.0.1:8000/api/departments/',params={"$dep_id_list":"T03,T04"})
# print(str.status_code)
# print(str.url)
# print(str.json())

# 查询学院 组合
# ：http://127.0.0.1:8000/api/departments/?slogan=Here is Slogan&master_name=Test-Master&dep_name=Test学院
# url="http://127.0.0.1:8000/api/departments/"
# params={"slogan":"Here is Slogan","master_name":"Test-Master","dep_name":"Test学院"}
# str=requests.get(url=url,params=params)
# print("url:",str.url)
# print(str.text)

# 学院新增
# data=json.dumps(         {
#                 "data": [
#                         {
#                             "dep_id":"T010_02",
#                             "dep_name":"Test01学院",
#                             "master_name":"Test-Master",
#                             "slogan":"Here is Slogan"
#                         }
#                   ]
#             })
#
# headers = {'content-type': 'application/json'}
# # str=requests.post("http://127.0.0.1:8000/api/departments/",data=data,headers=headers)
# # print("新增后数据为：",str.text)
#
# # 学院更新
# url="http://127.0.0.1:8000/api/departments/T010_02/"
# data=json.dumps(            {
#                 "data": [
#                         {
#                             "dep_id": "T010_02",
#                             "dep_name": "C-java学院",
#                             "master_name": "C++-Master",
#                             "slogan": "Here is Slogan"
#                         }
#                   ]
#             })
# str=requests.put(url=url,data=data,headers=headers)
# print(str.url)
# print(str.status_code)
# print(str.headers)
# str=str.text
# print(str)
# try:
#     assert "C-java学院" in str
#     print("断言成功")
# except:
#     print("失败")

# 删除学院
# url="http://127.0.0.1:8000/api/departments/T010_02/"
# str=requests.delete(url)
# print(str.status_code)
# print("请求url为：",str.url)
# print("返回值为：",str.text)
