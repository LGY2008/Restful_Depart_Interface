import requests
# 定义url
url="http://127.0.0.1:8000/api/departments/Test_0111/"
# 请求
r=requests.delete(url)
# 获取响应状态码
print(r.status_code)
# 以文本形式获取响应数据
print(r.text)