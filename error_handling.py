#异常处理
# def maxnum_error(maxNum):
#     if maxNum < 1:
#         raise ValueError("请输入一个大于零的总人数")
#     return maxNum

# def step_num(maxNum, stepNum):
#     if stepNum > maxNum:
#         raise ValueError("请输入一个小于总人数的间隔")
#     return stepNum

def step_num(stepNum):
    if stepNum < 1:
        raise ValueError("请输入大于零的间隔")
    return stepNum