from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox#QtWidgets:专门负责空键窗口图形功能 并导入几个类
#应用程序 主窗口 按钮 文本编辑框 弹出结果的对话框


def handleCalc():#slot:处理signal的函数
    info = textEdit.toPlainText() #通过toPlainText方法获取编辑框内的文本内容

# 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )

app = QApplication([]) #创建一个application的对象

window = QMainWindow() #创建一个主窗口对象
window.resize(500, 400) #窗口的宽度像素与高度像素
window.move(300, 310) #控制主窗口在显示器的位置
window.setWindowTitle('薪资统计') #把 薪资统计 设置在窗口的标题栏上

textEdit = QPlainTextEdit(window) #创建一个纯文本对象 主窗口window的副窗口
textEdit.setPlaceholderText("请输入薪资表") #设置纯文本对象的提示文本
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
button.clicked.connect(handleCalc)

window.show() #将以上设置的窗口展现在界面上

app.exec_() #一直循环等待输入信号