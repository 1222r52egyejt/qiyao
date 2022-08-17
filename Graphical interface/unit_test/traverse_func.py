from collections import deque



def traverse(start_id, stepNum, traverse_name):
 
    traverse_data = deque(traverse_name)
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
    return (list(delData) + list(result))
