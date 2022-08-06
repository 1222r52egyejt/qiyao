from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import os
from collections import deque
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
# self.ui = QUiLoader().load(path+'/ui/main.ui')
# print(path)

class Stats:

    def __init__(self):
       
# 从文件中加载UI定义  
        qfile_stats = QFile(path+'/Desktop/qiyao/Graphical interface/stats.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)

        # self.ui.button.clicked.connect(self.handleCalc)
        self.ui.Button.clicked.connect(self.traverse)
       
           
    def traverse(self):
    # def traverse(self, stepNum, start_id):
        
        info = self.ui.TextEdit.toPlainText()
       
        traverse_data = info.splitlines()
        for i in range(len(traverse_data)):
            traverse_data[i] = traverse_data[i].strip()
           
        print(traverse_data)
    #     delData = deque()
    #     if 0 <= start_id < len(traverse_data):
    #         traverse_data.rotate(-(start_id))
    #     elif start_id >= len(traverse_data):
    #         traverse_data.rotate(-(start_id % len(traverse_data)))
    #     else:
    #         # print('输入错误')
    #         # sys.exit(1)
    #         traverse_data.rotate(-(start_id %
    #                              len(traverse_data) + len(traverse_data) + 1))

    #     while len(traverse_data) > 1:
    #         traverse_data.rotate(-(stepNum-1))  # 左移stepNum-1次
    #         delData.append(traverse_data[0])
    #         traverse_data.popleft()  # 删除第stepNum元素
    #         result = traverse_data[0].split()
    #     return (list(delData)+ result)  


    # # QMessageBox.about(self.ui,
    # #                 '统计结果',
    # #                 f'''薪资20000 以上的有：\n{delData}
    # #                 \n薪资20000 以下的有：\n{result}'''
    # #                 )

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()