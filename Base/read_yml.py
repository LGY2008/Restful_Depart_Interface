import yaml,os
class ReadYaml():
    def __init__(self,file_name):
        self.file_name=os.getcwd()+os.sep+"Data"+os.sep+file_name

    def read_yaml(self):
        with open(self.file_name,"r",encoding="utf-8") as f:
            return yaml.load(f)

