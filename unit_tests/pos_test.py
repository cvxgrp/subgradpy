import unittest
import math
import __builtin__
from subgradpy import *


class testPos(unittest.TestCase):
    def test_get_value(self):
        x = var('x')
        ex = pos(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            if val>0:
                self.assertAlmostEqual(ex.get_value({'x':val}),val)
            else:
                self.assertAlmostEqual(ex.get_value({'x':val}),0.0)

    def test_subgrad(self):
        x = var('x')
        ex = pos(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            g = ex.subgrad({'x':val})
            if val>0:
                self.assertAlmostEqual(g['x'],1.0)
            elif val<0:
                self.assertAlmostEqual(g['x'],0.0)
            else:
                self.assertTrue(g['x']<=1)
                self.assertTrue(g['x']>=0)

if __name__=='__main__':
    unittest.main()
