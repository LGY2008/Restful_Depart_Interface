from Resources.resource_classes import ResourceClass
from Resources.resource_depart import ResourceDepart
from Resources.resource_students import ResourceStudent
class ResourceIn():
    # 学院统一入口类
    def get_depart(self):
        return ResourceDepart()
    # 班级统一入口类
    def get_class(self):
        return ResourceClass()
    # 学生统一入口类
    def get_student(self):
        return ResourceStudent()
