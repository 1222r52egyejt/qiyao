# import time
# from turtle import delay
from deque_travers_by_step import Person

# class Person:
#     def __init__(self, name, id, gender, age) -> None:
#         self.name = name 
#         self.id = id 
#         self.gender = gender
#         self.age = age

class public_use:
    def traverse(self, stepNum, start_id):   
        data = []
        del_data = []
        num = 0
        start_id  += 0
        #delay(2)
        for i in (self.name):
            data.append(i)

        while len(data) > 1:
            num += 1
            temp = data.pop(0)
            if num == stepNum:
                del_data.append(temp)
                num = 0
            else:
                data.append(temp)
        return(del_data, data[0])


class JosephusRing(public_use):
    
    def __init__(self)-> None:
        self.name = []

    def add_member(self, obj: Person):
        self.name.append(obj.name)
    # public_use.add_member(obj= Person)

    # def traverse(self, stepNum, start_id):   
    #     data = []
    #     del_data = []
    #     num = 0
    #     start_id  += 0
    #     #delay(2)
    #     for i in (self.name):
    #         data.append(i)

    #     while len(data) > 1:
    #         num += 1
    #         temp = data.pop(0)
    #         if num == stepNum:
    #             del_data.append(temp)
    #             num = 0
    #         else:
    #             data.append(temp)
    #     return(del_data, data[0])
    

# if __name__ == '_main_':
#         JosephusRing.traverse()
    