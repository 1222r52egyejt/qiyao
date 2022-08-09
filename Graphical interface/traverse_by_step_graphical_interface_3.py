from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from json import dump
from PySide2.QtWidgets import QFileDialog
from json import load
from json_zip import classB
import os
from collections import deque
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# self.ui = QUiLoader().load(path+'/ui/main.ui')
# print(path)
# print(classB.json_reader())
class Stats(QWidget):

    def __init__(self,parent=None):
       
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
        self.ui.pushButton.clicked.connect(self.getFiles)
           
    def traverse(self):
    # def traverse(self, stepNum, start_id):
    
    # #保存存入文件路径
    #     filePath, _  = QFileDialog.getSaveFileName(
    #     self.ui,             # 父窗口对象
    #     "保存文件", # 标题
    #     r"d:\\data",        # 起始目录
    #     "json类型 (*.json)" # 选择类型过滤项，过滤内容在括号中
    # )
    # #创建并写入
    #     with open(filePath, "w") as json_file:
    #         json_dict = dump(dict, json_file)

        info = self.ui.TextEdit.toPlainText()
        stepNum = self.ui.spinBox.value()
        start_id = self.ui.spinBox_2.value()
        traverse_data = info.splitlines()
        for i in range(len(traverse_data)):
            traverse_data[i] = traverse_data[i].strip()
            
        # print(traverse_data)
        delData = deque()
        traverse_data = deque(traverse_data)
    # print(traverse_data)
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
            # traverse_data.rotate(-(3-1))  # 左移stepNum-1次
            delData.append(traverse_data[0])
            traverse_data.popleft()  # 删除第stepNum元素
            result = traverse_data[0].split()
        # return (result)  

        QMessageBox.about(self.ui,
                            '统计结果',
                            f'''淘汰顺序为：\n{list(delData)}
                            \n最后剩下的是：\n{result}'''
                            )


    def getFiles(self):
        #实例化QFileDialog
        dig=QFileDialog()
        #设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        #文件过滤
        dig.setFilter(QDir.Files)

        if dig.exec_():
            #接受选中文件的路径，默认为列表
            filenames=dig.selectedFiles()
            #列表中的第一个元素即是文件路径，以只读的方式打开文件
            f=open(filenames[0],'r',encoding="UTF-8")

            with f:
                #接受读取的内容，并显示到多行文本框中
                data=f.read()

                self.ui.lineEdit.setText(str(filenames))
                self.ui.TextEdit.setPlainText(data)

        # def add_name(self):
        #     self.ui.TextEdit.appendPlainText('你好，白月黑羽')
       
if __name__ == '__main__':
    # app = QApplication([])
    # stats = Stats()
    # stats.ui.show()
    # app.exec_()

    app=QApplication(sys.argv)
    ex=Stats()
    ex.ui.show()
    sys.exit(app.exec_())