import unittest
import math
import __builtin__
from subgradpy import *

class testMin(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_value(self):
        x = var('x')
        ex = min(x);
        vals = [-1,5,12345.65,-12345678.0]
        self.assertEqual(ex.get_value({'x': vals}),__builtin__.min(vals))

    def test_supergrad(self):
        x = var('x');
        y = var('y');
        z = var('z');
        ex = min(x,y,z)
        g = ex.supergrad({'x':1.5,'y':-12.2,'z':-12.2})
        self.assertAlmostEqual(g['x'],0)
        self.assertAlmostEqual(g['y'],1)
        self.assertAlmostEqual(g['z'],1)

if __name__=='__main__':
    unittest.main()
