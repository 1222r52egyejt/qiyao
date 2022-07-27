from list_travers_by_step import JosephusRing
from list_travers_by_step import Person
###:检测可迭代对象

# 使用 collections包下的Iterable模块
# from collections import Iterable
# 然后使用一个方法isinstance
# print(isinstance(object,Iterable))
# 当返回True时说明是可迭代对象，返回False则不是，该方法输出控制台会抛出一个警告，并不是异常


# 例如:
# mylist = [1,2,3,4,5]
# print(isinstance(mylist,Iterable))


# ###:检测可迭代器
# # 使用collections包下的Iterator
# from collections import Iterator5
# # 同样使用isinstance方法
# print(isinstance(object,Iterator))
# # 当返回True时说明是迭代器，返回False则不是，该方法输出控制台会抛出一个警告，并不是异常

# #示例：
# print(isinstance(Person,Iterator))

#使用迭代器完成斐波那契数列
# 要想成为迭代器，首先必须是一个对象，所有class跑不了
class MyList():
    
     # 使用__init__方法定义属性
    # 并且实例对象之前要传进来一个参数，表示要查找的位数
    def __init__(self, n):
        # self.x： 用来记录迭代器每次迭代的位置
        # 因为斐波那契数列是有规律的，所有我们用a和b来模拟前两个数字，来算出后一个数字
        # self.a 为前两个数字
        # self.b 为前一个数字
        self.index, self.a, self.b, self.num = 0, 0, 1, n
        
    # 要想成为迭代器首先得先使用iter方法成为可迭代对象
    def __iter__(self):
        # 该方法要返回一个迭代器对象，因为自己就是迭代器，所有返回自身实例self
        return self
    
    # 要想成为迭代器，必须实现next方法，并且返回每次迭代出来的数据
    def __next__(self):
        # 在这里其其实self.num就是用户传过来的要查找的位数，那么也就是长度
        # 那么迭代器迭代的位置索引肯定不能大于长度
        if self.index < self.num:
            # 当要第一位数字的时候，我把b给a，因为b是1，然后b来算前两位的和，那么b=a+b=1，那么第二位就算出来了
            # 当要第三位的时候，此时b=a+b=1+1=2，然后再给a
            # 那么也就是说b起到的作用就是记录上一次的数字，并且算下一位的数字
            # 而a起到的作用是记录前两次的数字和返回给用户
            self.a, self.b = self.b, self.a + self.b
            # 迭代器迭代位置每次+1
            self.index+=1
            return self.a
        else:
            # 当大于或等于的时候就停止迭代
            raise StopIteration

# 最后调用
if __name__ == '__main__':
    while True:
        try:
            num = int(input("请输入要算的位数："))
        except:
            print("请输入正确的数字格式：")
        else:
            mylist = MyList(num)
            for item in mylist:
                print(item)
            break

        
        
