import yaml
data={
                "data": [
                        {
                            "dep_id":"T01",
                            "dep_name":"Test学院",
                            "master_name":"Test-Master",
                            "slogan":"Here is Slogan"
                        }
                  ]
      }
def write_yaml():
    with open("../Data/depart_add.yml","w",encoding="utf-8") as f:
        yaml.dump(data,stream=f,encoding="utf-8",allow_unicode=True)
if __name__ == '__main__':
    write_yaml()