from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import os
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
        self.ui.Button.clicked.connect(self.handleCalc)
       

    def handleCalc(self):
        info = self.ui.TextEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.ui,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()