import unittest
import math
import __builtin__
from subgradpy import *

class testSquarePos(unittest.TestCase):
    def test_get_value(self):
        x = var('x')
        ex = square_pos(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            if val>0:
                self.assertAlmostEqual(ex.get_value({'x':val}),val*val)
            else:
                self.assertAlmostEqual(ex.get_value({'x':val}),0.0)

    def test_subgrad(self):
        x = var('x')
        ex = square_pos(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            g = ex.subgrad({'x':val})
            self.assertAlmostEqual(g['x'],2*__builtin__.max(val,0))


if __name__=='__main__':
    unittest.main()
