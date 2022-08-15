# -*- coding: utf-8 -*-

import unittest
from traverse_func import *

with open(path+'/Desktop/unit_test_josephus.txt', "r", encoding='utf-8')as f:
                result=f.read()

with open(path+'/Desktop/start_id.txt', "r", encoding='utf-8')as f:
                start_id=int(f.read())

with open(path+'/Desktop/stepNum.txt', "r", encoding='utf-8')as f:
                stepNum=int(f.read())

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
        print ("traverse_function_test")
        self.assertEqual(result, str(traverse(start_id, stepNum)))

#输入(步长)测试
    def test_stepNum(self):
        print ("stepNum_in_test")
        if(stepNum > 0):
            return 1

        self.assertEqual(stepNum, 1)


if __name__ == '__main__':
    unittest.main(verbosity = 2)