
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
f = zipfile.ZipFile('yasuo.zip')
# f1 = f.getinfo('yasuo/hello.txt')   # hello.txt为压缩包中的一个文件
# f1.file_size#原文件大小
# f1.compress_size#压缩后文件大小
# print(f1.file_size)
# f.close()

#解压zip文件
# f.extractall()        #ZipFile对象的extractall()方法解压ZIP文件，压缩包中的文件都放到当前目录中。
f.extractall('jieya')         #也可以向该方法传递一个文件夹名称，它将解压后的文件都放到这个文件夹中。
# f.extract('yasuo/hello.txt')          # hello.txt为压缩包中的一个文件/解压单个文件
# # f.extarct('hello.txt', 'goodone')       # hello.txt为压缩包中的一个文件/也可以向该方法传递第二个参数，表示解压的文件夹
# f1 = f.open('yasuo/hello.txt',"r")
# print(f.namelist())
# f = open("jieya/yasuo/hello.txt", "r+")
with open("jieya/yasuo/hello.txt", "r+", encoding='utf-8') as f:
        print(f.readline())


# #创建并写入zip文件
# f = zipfile.ZipFile('yasuo.zip', 'w')         #如果需要压缩为ZIP文件，则需要以写模式打开ZipFile对象，即传入w作为第二个参数。
# f = write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)    #向该对象的write()方法传入一个路径名，即可压缩这个路径名所指的文件。该方法的第二个参数表示压缩算法。
# f = zipfile.ZipFile('yasuo.zip', 'ceshi.txt')         #如果需要将文件添加到已有的压缩文件中，则需要以添加模式打开这个ZIP文件。


