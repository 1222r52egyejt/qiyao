
import os
from collections import deque

path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
f =  open(path+'/Desktop/ceshi.txt', "r", encoding='utf-8')
                #接受读取的内容，并显示到多行文本框中
lines = f.readlines()
# print(lines)

def traverse(start_id, stepNum):
    
    traverse_data = deque(lines)
    delData = deque()
    if 0 <= start_id < len(traverse_data):
        traverse_data.rotate(-(start_id) - 1)
    elif start_id >= len(traverse_data):
        traverse_data.rotate(-(start_id % len(traverse_data) + 1))
    else:
        # print('输入错误')
        # sys.exit(1)
        traverse_data.rotate(-(start_id %
                            len(traverse_data) + len(traverse_data) + 1))

    while len(traverse_data) > 1:
        traverse_data.rotate(-(stepNum-1))  # 左移stepNum-1次
        delData.append(traverse_data[0])
        traverse_data.popleft()  # 删除第stepNum元素
        result = traverse_data[0].split()
    return (result)

# print(traverse(0,3))