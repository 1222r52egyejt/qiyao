from fileinput import filename
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from json import dump
from PySide2.QtWidgets import QFileDialog
import os
from collections import deque
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
class Stats(QWidget):

    def __init__(self):
        qfile_stats = QFile(path+'/Desktop/qiyao/Graphical interface/stats.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close
    
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.Button.clicked.connect(self.traverse)
        self.ui.pushButton.clicked.connect(self.getFiles)
        self.ui.pushButton_4.clicked.connect(self.saveFiles)
           
    def traverse(self):
    # def traverse(self, stepNum, start_id):

        info = self.ui.TextEdit.toPlainText() #获取文本框中的内容
        stepNum = self.ui.spinBox.value() #获取步长
        start_id = self.ui.spinBox_2.value() #获取起始位置
        traverse_data = info.splitlines()
        for i in range(len(traverse_data)):
            traverse_data[i] = traverse_data[i].strip()
            
    
        delData = deque()
        traverse_data = deque(traverse_data)

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
       

        QMessageBox.about(self.ui,
                            '统计结果',
                            f'''淘汰顺序为：\n{list(delData)}
                            \n最后剩下的是：\n{result}'''
                            )
        # print(type(info))  

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

                self.ui.lineEdit.setText(filenames[0])
                self.ui.TextEdit.setPlainText(data)
        # print(filenames[0])
    def saveFiles(self):
        #实例化QFileDialog
        dig=QFileDialog()
        #设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        #文件过滤
        dig.setFilter(QDir.Files)

        if dig.exec_():
            #接受选中文件的路径，默认为列表
            filenames=dig.selectedFiles()
        info = self.ui.TextEdit.toPlainText() #获取文本框中的内容
        dict = info
        # with open(filenames[0], "w") as json_file:
        #     json_dict = dump(dict, json_file)
        with open(filenames[0], "w", encoding='utf-8')as f:
            f.write(dict)
        # print(json_dict)
       
if __name__ == '__main__':
    # app = QApplication([])
    # stats = Stats()
    # stats.ui.show()
    # app.exec_()

    app=QApplication(sys.argv)
    ex=Stats()
    ex.ui.show()
    sys.exit(app.exec_())