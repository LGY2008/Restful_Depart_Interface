import os,sys
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
        return ReadYaml( "depart_get_data.yml" ).read_yaml().get( "text_depart_all" )
class TestDepart():
    def setup_class(self):
        # 实例化统一入口类 并得到学院对象
        self.res=ResourceIn().get_depart()
    # 新增学院
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
    # 查询学院_所有
    # def test_get_depart(self):
    #     # 查询学院所有
    #     result=self.res.resource_get_depart_all()
    #     try:
    #         assert get_data("get").get("expect_status") == result.get("status"),"断言响应状态码出错！"
    #         assert get_data("get").get("expect_text") in result.get("text"),"断言文本出错"
    #     except:
    #         print("断言出错")
    #         raise

