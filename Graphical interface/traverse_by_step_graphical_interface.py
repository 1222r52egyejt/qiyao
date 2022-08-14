from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from time import time 
# from log import logger
# from log import rf_handler
# import datetime

from logger import logger_config
from PySide2.QtWidgets import QFileDialog
import os
from collections import deque
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
result = str
class Stats(QWidget):

    def __init__(self):
        qfile_stats = QFile(path+'/Desktop/qiyao/Graphical interface/stats.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close
    
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.Button_josephus.clicked.connect(self.traverse)
        self.ui.pushButton_select.clicked.connect(self.getFiles)
        self.ui.pushButton_save.clicked.connect(self.saveFiles)
        self.ui.pushButton_save.clicked.connect(self.result_check)
           
    def traverse(self):
    # def traverse(self, stepNum, start_id):
        # start = datetime.datetime.now
        start = time()
        try: 
            info = self.ui.TextEdit_josephus.toPlainText() #获取文本框中的内容
            stepNum = self.ui.spinBox_step.value() #获取步长
            start_id = self.ui.spinBox_start_id.value() #获取起始位置
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
                stop = time()
                # stop = datetime.datetime.now
            # print(f'一共耗费了{(stop - start):.20f}秒。')
            self.ui.TextEdit_svrvivor.setPlainText(str(result))
            self.ui.TextEdit_pass_order.setPlainText(str(list(delData)))
            self.ui.TextEdit_timelast.setPlainText(f'{(stop - start):.20f}')

        
        except:
            # logger.addHandler(rf_handler)
            logger = logger_config(log_path=path+'/Desktop/qiyao/Graphical interface/log.txt', logging_name='josephus_log')
            logger.error("输入数据为空")
            # print("输入数据不能为空")

       

        
    #读取文件
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
        
            with open(filenames[0], "r", encoding='utf-8')as f:
                #接受读取的内容，并显示到多行文本框中
                data=f.read()
       

            self.ui.select_lineEdit.setText(filenames[0])
            self.ui.TextEdit_josephus.setPlainText(data)

    #保存需要遍历的信息到文件   
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
            info = self.ui.TextEdit_josephus.toPlainText() #获取文本框中的内容
            dict = info
        # with open(filenames[0], "w") as json_file:
        #     json_dict = dump(dict, json_file)
            # if (filename[0]):
            try:
                with open(filenames[0], "w", encoding='utf-8')as f:
                        f.write(dict)
                self.ui.save_lineEdit.setText(filenames[0])
            except FileNotFoundError:
                # logger = logger_config(log_path=path+'/Desktop/qiyao/Graphical interface/log.txt', logging_name='josephus_log')
                # logger.error("找不到文件")
                pass

    def result_check(self):
    #实例化QFileDialog
       
        info = self.ui.TextEdit_svrvivor.toPlainText() #获取文本框中的内容
        dict = info
    
        with open(path+'/Desktop/unit_test_josephus.txt', "w", encoding='utf-8')as f:
                    f.write(dict)

       
if __name__ == '__main__':

    app=QApplication(sys.argv)
    ex=Stats()
    ex.ui.show()
    sys.exit(app.exec_())