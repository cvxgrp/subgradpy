import unittest
from subgradpy import *

class TestAbs(unittest.TestCase):
    def setUp(self):
        x = var('x')
        self.ex = abs(x)

    def test__value_positive(self):
        self.assertEqual(self.ex.get_value({'x': 3}),3)
    
    def test_value_negative(self):
        self.assertEqual(self.ex.get_value({'x': -3}),3)

    def test_subgrad_positive(self):
        subgrad = self.ex.subgrad({'x':314})
        self.assertEqual(subgrad['x'],1)

    def test_subgrad_negative(self):
        subgrad = self.ex.subgrad({'x':-314})
        self.assertEqual(subgrad['x'],-1)
    
    def test_subgrad_zero(self):#should return a number between 0-1
        subgrad = self.ex.subgrad({'x':0})
        self.assertTrue(subgrad['x']<=1)
        self.assertTrue(subgrad['x']>=-1)


if __name__=='__main__':
    unittest.main()
