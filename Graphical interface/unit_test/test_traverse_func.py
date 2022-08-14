# -*- coding: utf-8 -*-

import unittest
from traverse_func import *

with open(path+'/Desktop/unit_test_josephus.txt', "r", encoding='utf-8')as f:
                #接受读取的内容，并显示到多行文本框中
                data=f.read()

class TestTraverseFunc(unittest.TestCase):
    """Test mathfuc.py"""
  
    def setUp(self):
        print ("do something before test.Prepare environment.")

    def tearDown(self):
        print ("do something after test.Clean up.")
 

    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")

#约瑟夫遍历功能测试
    def test_traverse(self):
        """Test method add(a, b)"""
        print ("traverse")
        self.assertEqual(data, str(traverse(0, 3)))
 

if __name__ == '__main__':
    unittest.main(verbosity = 2)