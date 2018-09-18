import requests,urllib3
# http=urllib3.PoolManager()
# h=http.request("GET","http://www.baidu.com")
# print(h.status)
# print(h.data)

r=requests.get("http://www.baidu.com")
print(type(r.content))