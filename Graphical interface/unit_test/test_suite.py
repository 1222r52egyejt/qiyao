# -*- coding: utf-8 -*-
import os
path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
import unittest
from test_traverse_func import TestTraverseFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTraverseFunc))

    with open(path+'/Desktop/qiyao/Graphical interface/unit_test/UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)