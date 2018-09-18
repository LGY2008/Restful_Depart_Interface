import yaml,os,sys
sys.path.append(os.getcwd())
class ReadYaml():
    # def __init__(self,file_name):
    #     self.file_name=os.getcwd()+os.sep+"Data"+os.sep+file_name
    #
    # def read_yaml(self):
    #     with open(self.file_name,"r",encoding="utf-8") as f:
    #         return yaml.load(f)

    def read_yaml1(self):
        with open("../Data/depart_data.yml","r",encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    print(ReadYaml().read_yaml1().get("text_depart_add").get("data")[0].get("dep_id"))