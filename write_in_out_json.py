
import json

#读取json文件

# with open("test.json", "r") as json_file:
#         json_dict = json.load(json_file)
#         print(json_dict)
#         print("type(json_dict) = >", type(json_dict))
#         print(json.dumps(json_dict, indent=4))


#创建并写入json文件

dict = ['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ]

with open("test.json", "w") as json_file:
        json_dict = json.dump(dict, json_file)



