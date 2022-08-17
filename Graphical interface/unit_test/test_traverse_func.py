
import unittest
from traverse_func import *


class TestTraverseFunc(unittest.TestCase):
  
#约瑟夫功能测试
    def test_josefu_function(self):
        print ("josefu_function_test")
        traverse_name = ['小王','红红','小明','小曹','曹总','然然']
        expect_order = ['红红','小明','小曹','曹总','然然','小王']

        self.assertEqual(expect_order, traverse(0, 1, traverse_name))

#输入(stepNum)测试
    def test_stepNum(self):
        print ("stepNum_test")
        traverse_name = ['小王','红红','小明','小曹','曹总','然然']
        expect_order = ['小曹','小王','曹总','小明','然然','红红']

        self.assertEqual(expect_order, traverse(0, 3, traverse_name))

#输入(start_id)测试
    def test_start_id(self):
        print ("start_id_test")
        traverse_name = ['小王','红红','小明','小曹','曹总','然然']
        expect_order = ['小明','然然','小曹','红红','曹总','小王']

        self.assertEqual(expect_order, traverse(-1, 3, traverse_name))

#上边界测试
    def test_upper_border(self):
        print ("upper_border_test")
        traverse_name = ['小王','红红','小明','小曹','曹总','然然']
        expect_order = ['红红','小明','小曹','曹总','然然','小王']

        self.assertEqual(expect_order, traverse(6, 1, traverse_name))
#下边界测试
    def test_lower_border(self):
        print ("lower_border_test")
        traverse_name = ['小王','红红','小明','小曹','曹总','然然']
        expect_order = ['小王','红红','小明','小曹','曹总','然然']

        self.assertEqual(expect_order, traverse(-7, 1, traverse_name))



if __name__ == '__main__':
    unittest.main(verbosity = 2)