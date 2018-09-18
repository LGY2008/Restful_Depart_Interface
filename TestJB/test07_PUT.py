import json
import requests
# 定义url
url="http://127.0.0.1:8000/api/departments/T0111/"
# 定义报文
data={
            "data": [
                      {
                        "dep_id": "T0111",
                        "dep_name": "Test学院updata",
                        "master_name": "Test-Master",
                        "slogan": "Here is Slogan"
                      }
                    ]
        }
# 指定请求信息头
headers={'content-type': 'application/json'}
# 请求
r=requests.put(url,data=json.dumps(data), headers=headers)
# 获取响应状态码
print(r.status_code)
# 以文本形式获取响应数据
print(r.text)