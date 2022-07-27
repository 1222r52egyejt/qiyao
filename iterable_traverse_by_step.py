from collections import deque
from deque_travers_by_step import circle


class MyList():
    
    def __init__(self, stepNum):
        # self.x： 用来记录迭代器每次迭代的位置
        
        self.index, self.del_data, self.traverse_data, self.stepNum = 0, 'xiexie', deque(circle), stepNum
        
    # 要想成为迭代器首先得先使用iter方法成为可迭代对象
    def __iter__(self):
        # 该方法要返回一个迭代器对象，因为自己就是迭代器，所有返回自身实例self
        return self
    
    # 要想成为迭代器，必须实现next方法，并且返回每次迭代出来的数据
    def __next__(self):
        # 在这里其其实self.num就是用户传过来的要查找的位数，那么也就是长度
        # 那么迭代器迭代的位置索引肯定不能大于长度
 
        if self.index < len(circle):
            
            # stepNum = 3
            # del_data = deque()
            self.traverse_data.rotate(-(self.stepNum - 1)) #左移stepNum-1次
            # del_data.append(self.traverse_data[0])
            self.del_data = self.traverse_data.popleft()      #删除第stepNum元素
        
            self.index += 1
            return self.del_data
        else:
            raise StopIteration
# 最后调用
if __name__ == '__main__':
    while True:
        try:
            step = int(input("请输入跳过的人数："))
        except:
            print("请输入正确的数字格式：")
        else:
            mylist = MyList(step)
            for item in mylist:
                print(item)
            break