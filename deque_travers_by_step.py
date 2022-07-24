# import sys
from collections import deque

# from turtle import circle
class public:
     def traverse(self, stepNum, start_id):
    #  def choiceNum(self, stepNum, start_id, maxNum):    
        # data = deque(['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ])
        # data = deque(range(maxNum))
        # data = deque(range(44444))
        data = deque(self.name)
        delData = deque()
        if 0 <= start_id < len(data):
            data.rotate(-(start_id))
        elif start_id >= len(data):
        # data.rotate(-(len(data) - start_id - 1))
            data.rotate(-(start_id % len(data)))
        else :
            # print('输入错误')
            # sys.exit(1)
            data.rotate(-(start_id % len(data) + len(data) + 1))

        while len(data) > 1:
            data.rotate(-(stepNum-1)) #左移stepNum-1次
            #delData.append(data[0])
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
    # public_use.add_member(obj= Person)
        
    # def traverse(self, stepNum, start_id):
    # #  def choiceNum(self, stepNum, start_id, maxNum):    
    #     # data = deque(['小明', '小梅', '小李', '小王', '小陈', 'kitty', 'hellokitty', '小红','曹总', '小曹' ])
    #     # data = deque(range(maxNum))
    #     # data = deque(range(44444))
    #     data = deque(self.name)
    #     delData = deque()
    #     if 0 <= start_id < len(data):
    #         data.rotate(-(start_id))
    #     elif start_id >= len(data):
    #     # data.rotate(-(len(data) - start_id - 1))
    #         data.rotate(-(start_id % len(data)))
    #     else :
    #         # print('输入错误')
    #         # sys.exit(1)
    #         data.rotate(-(start_id % len(data) + len(data) + 1))

    #     while len(data) > 1:
    #         data.rotate(-(stepNum-1)) #左移stepNum-1次
    #         #delData.append(data[0])
    #         delData.append(data[0])
    #         data.popleft()      #删除第stepNum元素
    #     return  (delData, data[0])
      
# if __name__ == '_main_':
#     public.traverse() 


