# import deque_travers_by_step
# import list_travers_by_step
from tracemalloc import stop
from main import classA
# import datetime
import time



def time_master():     
    print('开始运行程序...')
    start = time.time()
    # start = datetime.datetime.now
    classA.traverse(3, 0)
    stop = time.time()
    # stop = datetime.datetime.now
    print('程序结束运行...')
    print(f'一共耗费了{(stop - start):.20f}秒。')
    

time_master()


if __name__ == '_main_':
    time_master() 