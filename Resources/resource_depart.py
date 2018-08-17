import json

from Base.base_tools import BaseTools
import Resources
class ResourceDepart(BaseTools):
    # 拼接url 封装
    def resource_condition(self,condition=None,id=None):
        if condition is not None:
            url=Resources.depart_url_all+"?"+condition
            return self.get_method( url )
        elif id is not None:
            # 拼接url 查询指定、更新、删除 使用
            url = Resources.depart_url_all + id + '/'
            return url
    #  学院查询所有
    def resource_get_depart_all(self):
        # 查询学院 所有
        return self.get_method(Resources.depart_url_all)
    # 学院查询 指定
    def resource_get_depart_one(self,id):
        url=self.resource_condition(id=id)
        return self.get_method(url)
    # 学院查询 list
    def resource_get_depart_list(self,condition):
        return self.resource_condition( condition=condition )
    # 学院查询 模糊
    def resource_get_depart_partial(self,condition):
        return self.resource_condition( condition=condition )
    # 学院查询 组合
    def resource_get_depart_combo(self,condition):
        return self.resource_condition( condition=condition )
    # 学院新增
    def resource_add_depart(self,data):
        # 获取url
        url=Resources.depart_url_all
        return self.post_method(url,data)
    # 学院更新
    def resource_update_depart(self,id,data):
        # id:要更新的资源；data:更新的json串
        url=self.resource_condition(id=id)
        return self.put_method(url,data)
    # 学院删除
    def resource_delete_depart(self,id):
        # id要删除的资源
        url = self.resource_condition( id=id )
        return self.delete_method(url)
    # 获取响应id
    def resource_get_depid(self,dect):
        dect=json.load(dect)
        str=dect.get("create_success").get("results")[0]
        print("json.load值为：",str)
        return str
