# import sys
from collections import deque
import json
import zipfile


# #使用json库打开json文件中的内容
# with open("test.json", "r") as json_file:
#         circle = json.load(json_file)
        

#使用zip库打开zip文件中的内容
#读取zip文件
f = zipfile.ZipFile('yasuo.zip')        #首先，通过zipfile.ZipFile()函数，创建ZipFile对象。

#解压zip文件
f.extractall('jieya')         #也可以向该方法传递一个文件夹名称，它将解压后的文件都放到这个文件夹中。

with open("jieya/yasuo/hello.txt", "r+", encoding='utf-8') as f:
        circle_in_document = f.readline()
        circle = circle_in_document.split(',')

##

class public:
     def traverse(self, stepNum, start_id):
        data = deque(list(circle))
        # data = deque()
        # for i in range(44444):
        #     data.append(i)
        delData = deque()
        if 0 <= start_id < len(data):
            data.rotate(-(start_id))
        elif start_id >= len(data):
            data.rotate(-(start_id % len(data)))
        else :
            # print('输入错误')
            # sys.exit(1)
            data.rotate(-(start_id % len(data) + len(data) + 1))

        while len(data) > 1:
            data.rotate(-(stepNum-1)) #左移stepNum-1次
            delData.append(data[0])
            data.popleft()      #删除第stepNum元素
        return  (delData, data[0])

class Person:
    def __init__(self, name, id, gender, age) -> None:
        self.name = name 
        self.id = id 
        self.gender = gender
        self.age = age

class JosephusRing(public):
      
    def __init__(self)-> None:
        self.name = deque()

    def add_member(self, obj: Person):
        self.name.append(obj.name)
    
if __name__ == '_main_':
    JosephusRing.traverse() 

