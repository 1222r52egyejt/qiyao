# import sys
from collections import deque
import json
from turtle import circle

with open("test.json", "r") as json_file:
        circle = json.load(json_file)
        # print(json_dict)
        # print("type(json_dict) = >", type(json_dict))
        # print(json.dumps(json_dict, indent=4))


class public:
     def traverse(self, stepNum, start_id):
        data = deque(circle)
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

