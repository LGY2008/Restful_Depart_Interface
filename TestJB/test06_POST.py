import json
import unittest

import requests
class Test01(unittest.TestCase):
    def test001(self):
        # 定义url
        url="http://127.0.0.1:8000/api/departments/"
        # 定义报文
        data={
                    "data": [
                              {
                                "dep_id": "T0111",
                                "dep_name": "Test学院",
                                "master_name": "Test-Master",
                                "slogan": "Here is Slogan"
                              }
                            ]
                }
        # 指定请求信息头
        headers={'content-type': 'application/json'}
        # 请求
        r=requests.post(url,data=json.dumps(data), headers=headers)
        r.encoding="utf-8"
        # 获取响应状态码
        print(r.status_code)
        # 以文本形式获取响应数据
        # text=r.text
        # print(text)
        j=r.json()
        expect_result={"already_exist":{"count":0,"results":[]},"create_success":{"count":1,"results":[{"dep_id":"T0111","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}}
        # print(expect_result.get("create_success").get("count"))
        # self.assertDictEqual(j,expect_result)
        assert j == expect_result
if __name__ == '__main__':
    unittest.main()
