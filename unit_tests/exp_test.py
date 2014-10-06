import unittest
import math
from subgradpy import *

class TestExp(unittest.TestCase):
    def setUp(self):
        self.x_values = [-5,0,42,123];
        x = var('x')
        self.ex = exp(x)

    def test_get_value(self):
        for val in self.x_values:
            self.assertAlmostEqual(self.ex.get_value({'x': val}),
                                   math.exp(val))
    
    def test_subgrad(self):       
        for val in  self.x_values:
            g = self.ex.subgrad({'x':val})
            self.assertAlmostEqual(g['x'],math.exp(val))

if __name__=='__main__':
    unittest.main()
