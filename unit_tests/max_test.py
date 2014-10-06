import unittest
import math
import __builtin__
from subgradpy import *

class testMax(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_value(self):
        x = var('x')
        ex = max(x);
        vals = [-1,5,12345.65,-12345678.0]
        self.assertEqual(ex.get_value({'x': vals}),__builtin__.max(vals))

    def test_subgrad(self):
        x = var('x');
        y = var('y');
        z = var('z');
        ex = max(x,y,z)
        g = ex.subgrad({'x':1.5,'y':12.2,'z':12.2})
        self.assertAlmostEqual(g['x'],0)
        self.assertAlmostEqual(g['y'],1)
        self.assertAlmostEqual(g['z'],1)

if __name__=='__main__':
    unittest.main()
