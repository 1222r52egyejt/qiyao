# import sys
from collections import deque
from json import load
from zipfile import ZipFile



# #使用json库打开json文件中的内容
# with open("test.json", "r") as json_file:
#         circle = load(json_file)  
        

#使用zip库打开zip文件中的内容
#读取zip文件
f = ZipFile('yasuo.zip')        #首先，通过zipfile.ZipFile()函数，创建ZipFile对象。

#解压zip文件
f.extractall('jieya')         #也可以向该方法传递一个文件夹名称，它将解压后的文件都放到这个文件夹中。

with open("jieya/yasuo/hello.txt", "r+", encoding='utf-8') as f:
        circle_in_document = f.readline()
        circle = circle_in_document.split(',')

##

class public_traverse:
     def traverse(self, stepNum, start_id):
        traverse_data = deque(circle)
        # traverse_data = deque()
        # for i in range(44444):
        #     traverse_data.append(i)
        delData = deque()
        if 0 <= start_id < len(traverse_data):
            traverse_data.rotate(-(start_id))
        elif start_id >= len(traverse_data):
            traverse_data.rotate(-(start_id % len(traverse_data)))
        else :
            # print('输入错误')
            # sys.exit(1)
            traverse_data.rotate(-(start_id % len(traverse_data) + len(traverse_data) + 1))

        while len(traverse_data) > 1:
            traverse_data.rotate(-(stepNum-1)) #左移stepNum-1次
            delData.append(traverse_data[0])
            traverse_data.popleft()      #删除第stepNum元素
        return  (delData, traverse_data[0])

class Person:
    def __init__(self, name, id, gender, age) -> None:
        self.name = name 
        self.id = id 
        self.gender = gender
        self.age = age

class JosephusRing(public_traverse):
      
    def __init__(self)-> None:
        self.name = deque()

    def add_member(self, obj: Person):
        self.name.append(obj.name)
    
if __name__ == '_main_':
    JosephusRing.traverse() 

        