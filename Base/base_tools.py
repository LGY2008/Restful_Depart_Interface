import json
import requests
class BaseTools():
    # 获取结果
    def get_result(self,str):
        """
        :param str: 服务器响应结果
        :return: 返回字典格式 键名内容：url、status、json、text、headers
        """
        result={}
        # 请求rul
        result['url']=str.url
        # 服务器响应HTTP状态码
        result['status']=str.status_code
        # 响应数据为json格式
        result['json']=str.json()
        # 响应数据为text格式
        result['text']=str.text
        # 响应信息头
        result['headers']=str.headers
        # 以字节的方式
        result['content']=str.content
        # 编码格式
        result['encoding']=str.encoding
        # 返回字典
        return result
    # 查询接口
    def get_method(self,url,params=None):
        """
        :param url: 请求接口地址
        :param params: 带参数请求，格式为字典 如：{"id":"T01"}
        :return: 返回字典格式 键名内容：url、status、json、text、headers
        """
        str=None
        # 调用 get方法
        str=requests.get(url,params,timeout=5)
        # 返回响应结果
        return self.get_result(str)
    # 新增接口
    def post_method(self,url,data=None):
        """
        :param url: 请求url
        :param data: json报文，格式为字典
        :return: 返回字典格式 键名内容：url、status、json、text、headers
        """
        if data is not None:
            # 序列化将字典转化为通用的json格式
            data=json.dumps(data)
        # 设置信息头
        headers = {'content-type': 'application/json'}
        # 调用post方法
        str=requests.post(url=url,data=data,headers=headers,timeout=5)
        # 返回 响应结果
        return self.get_result(str)
    # 更新接口
    def put_method(self,url,data):
        """
        :param url:
        :param data:
        :return: 返回字典格式 键名内容：url、status、json、text、headers
        """
        if data is not None:
            # 序列化将字典转化为通用的json格式
            data=json.dumps(data)
        # 设置信息头
        headers = {'content-type': 'application/json'}
        # 调用put方法
        str=requests.put(url=url,data=data,headers=headers,timeout=5)
        # 返回响应结果
        return self.get_result(str)
    # 删除接口
    def delete_method(self,url):
        """
        :param url: 请求url
        :return: 返回字典格式 键名内容：url、status、json、text、headers
        """
        # 调用 delete方法
        str=requests.delete(url=url)
        # 返回响应结果
        # return self.get_result(str)
        return str
