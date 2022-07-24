# from deque_travers_by_step import JosephusRing
# from deque_travers_by_step import Person
from list_travers_by_step import JosephusRing
from list_travers_by_step import Person



classA = JosephusRing()
A = Person('Mary', 1, 'F', 1)
B = Person('cao', 2 , 'F', 2)
C = Person('shi', 3 , 'M', 3)
D = Person('ting', 4 , 'M', 4)
E = Person('ke', 5 , 'M', 5)
F = Person('ai', 6 , 'F', 6)
G = Person('de', 7 , 'M', 7)
classA.add_member(A)
classA.add_member(B)
classA.add_member(C)
classA.add_member(D)
classA.add_member(E)
classA.add_member(F)
classA.add_member(G)


    # print(list(classA.name))
print(classA.traverse(3, 0))

    # print(classA.traverse(3))
if __name__ == '_main_':
    JosephusRing.traverse() 


