
# import json

import zipfile

# #读取json文件

# # with open("test.json", "r") as json_file:
# #         json_dict = json.load(json_file)
# #         print(json_dict)
# #         print("type(json_dict) = >", type(json_dict))
# #         print(json.dumps(json_dict, indent=4))


# #创建并写入json文件

# dict = ['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ]

# with open("test.json", "w") as json_file:
#         json_dict = json.dump(dict, json_file)



#读取zip文件
f = zipfile.ZipFile('yasuo.zip')        #首先，通过zipfile.ZipFile()函数，创建ZipFile对象。

#解压zip文件
f.extractall('jieya')         #也可以向该方法传递一个文件夹名称，它将解压后的文件都放到这个文件夹中。

with open("jieya/yasuo/hello.txt", "r+", encoding='utf-8') as f:
        circle = f.readline()

print(circle)




