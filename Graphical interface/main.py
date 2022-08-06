from PySide2.QtUiTools import QUiLoader #加载器

class Stats():
    def __init__(self):
	    # 加载UI文件
        self.ui = QUiLoader().load(".\\main.ui") 