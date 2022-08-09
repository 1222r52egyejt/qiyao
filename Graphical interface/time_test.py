from traverse_by_step_graphical_interface_3 import Stats
# import datetime
from time import time
import sys
from PySide2.QtWidgets import QApplication

classA = Stats()

def time_master():     
    print('开始运行程序...')
    start = time()
    # start = datetime.datetime.now
    print(classA.traverse())
    stop = time()
    # stop = datetime.datetime.now
    print('程序结束运行...')
    print(f'一共耗费了{(stop - start):.20f}秒。')
    

time_master()


if __name__ == '_main_':
    time_master() 

    app=QApplication(sys.argv)
    ex=Stats()
    ex.ui.show()
    sys.exit(app.exec_())