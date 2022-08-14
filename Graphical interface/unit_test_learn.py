import unittest
import os
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
 
with open(path+'/Desktop/unit_test_josephus.txt', "r", encoding='utf-8')as f:
                #接受读取的内容，并显示到多行文本框中
                data=f.read()

class TestMathFunc(unittest.TestCase):

    def test_traverse(self):
        self.assertEqual(str(['薛蟠']), data)
       
if __name__ == '__main__':
    unittest.main()

