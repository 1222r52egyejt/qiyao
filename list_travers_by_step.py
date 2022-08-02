from deque_travers_by_step import Person
# from deque_travers_by_step import circle
from json_zip import classB

class public_traverse:
    def traverse(self, stepNum, start_id):   
        traverse_data = []
        del_data = []
        num = 0
        start_id  += 0
        #delay(2)
        # for i in (circle):
        #     traverse_data.append(i)
        # traverse_data = iter(classB.json_reader())    
        traverse_data = list(classB.json_reader())   
        # for i in range(44444):
        #     traverse_data.append(i)

        while len(traverse_data) > 1:
            num += 1
            temp = traverse_data.pop(0)
            if num == stepNum:
                del_data.append(temp)
                num = 0
            else:
                traverse_data.append(temp)
        return(del_data, traverse_data[0])


class JosephusRing(public_traverse):
    
    def __init__(self)-> None:
        self.name = []

    def add_member(self, obj: Person):
        self.name.append(obj.name)
    
if __name__ == '_main_':
    JosephusRing.traverse() 
