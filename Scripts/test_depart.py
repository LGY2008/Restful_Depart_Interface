import os,sys

import pytest

sys.path.append(os.getcwd())
from Resources.resource_in import ResourceIn
from Base.read_yml import ReadYaml
# 读取数据 格式封装
def get_data(method):
    if method=="get":
        return ReadYaml("depart_data.yml").read_yaml().get("text_depart_get_all")
    elif method=="post":
        return ReadYaml( "depart_data.yml" ).read_yaml().get( "text_depart_add" )
    elif method=="put":
        return ReadYaml( "depart_data.yml" ).read_yaml().get( "text_depart_all" )
    elif method=="delete":
        return ReadYaml( "depart_data.yml" ).read_yaml().get( "text_depart_add" ).get("data")[0].get("dep_id")
class TestDepart():
    def setup_class(self):
        # 实例化统一入口类 并得到学院对象
        self.res=ResourceIn().get_depart()
        print("获取新增ID：",get_data("delete"))

    # 新增学院
    @pytest.mark.run(order=1)
    def test_add_depart(self):
        try:
            result=self.res.resource_add_depart(get_data("post"))
            #获取新增状态码
            status=result.get("status")
            assert 201 == status,"断言新增响应码出错！"
            print("新增返回状态码：",status)
        except:
            print("出错了")
            raise
    # 查询学院_指定
    @pytest.mark.run(order=2)
    def test_get_depart_one(self):
        result=self.res.resource_get_depart_one(get_data("delete"))
        try:
            print("查询指定获取结果", result.get("json").get("dep_id"))
            # 断言响应报文
            assert get_data("delete") == result.get("json").get("dep_id")
            # 断言响应状态码
            assert 200 == result.get("status")
            print("查询指定成功，新增成功！")
        except:
            print("查询指定出错，新增失败！")
    # 查询学院_所有
    @pytest.mark.run(order=3)
    def test_get_depart(self):
        # 查询学院所有
        result=self.res.resource_get_depart_all()
        try:
            assert get_data("get").get("expect_status") == result.get("status"),"断言响应状态码出错！"
            print(result.get("status"))
            assert get_data("get").get("expect_text") in result.get("text"),"断言文本出错"
            print("查询所有学院成功...")
        except:
            print("查询所有学院失败...")
            raise
    # 删除学院
    @pytest.mark.run(order=4)
    def test_delete_depart(self):
        result=self.res.resource_delete_depart(get_data("delete"))
        print("删除URL为：",result.status_code)
        try:
            assert 204 == result.status_code
            print("删除新增学院，成功！")
        except:
            print("删除新增学院！")
            print(result.get("url"))
            print(result.get("status"))
