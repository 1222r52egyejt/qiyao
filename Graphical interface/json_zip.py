
from json import load
from json import dump
from json import dumps

from zipfile import ZipFile

class jsonreader:
        def __init__(self, json_filename):
                self.json_filename = json_filename
        def json_reader(self):
                with open(self.json_filename) as json_dict: 
                        jsonReader = load(json_dict)
                return jsonReader
classB = jsonreader("test.json")
# print(classB.json_reader())

# class zipreader:
#         def __init__(self, zip_filename):
#                 self.yasuo = zip_filename
#         def zip_reader(self):
#                 zip_dict = ZipFile('self.yasuo') #这里把yasuo换成了self.zip_filename
#                 zip_dict.extractall('jieya')
#                 with open("jieya/self.yasuo/hello.txt", "r+", encoding='utf-8') as zip_dict:
#                         zip_reader = zip_dict.readline()
#                 return zip_reader                                          
# # # 读取json文件

# with open("test.json", "r") as json_file:
#         json_dict = load(json_file)
#         print(json_dict)
#         print("type(json_dict) = >", type(json_dict))
#         print(dumps(json_dict, indent=4))


#创建并写入json文件

# dict = ['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ]

# # with open("test.json", "w") as json_file:
# #         json_dict = dump(dict, json_file)

# with open("self.json_filename", "w") as json_file:
#         json_dict = dump(dict, json_file)


# #读取zip文件
# f = ZipFile('yasuo.zip')        #首先，通过zipfile.ZipFile()函数，创建ZipFile对象。

# #解压zip文件
# f.extractall('jieya')         #也可以向该方法传递一个文件夹名称，它将解压后的文件都放到这个文件夹中。

# with open("jieya/yasuo/hello.txt", "r+", encoding='utf-8') as f:
#         circle = f.readline()

# print(circle)




