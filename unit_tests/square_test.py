import unittest
import math
from subgradpy import *

class testSquare(unittest.TestCase):
    def test_get_value(self):
        x = var('x')
        ex = square(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            self.assertAlmostEqual(ex.get_value({'x':val}),val*val)

    def test_subgrad(self):
        x = var('x')
        ex = square(x)
        x_vals = [ -3.14, 0.0, 123.456]
        for val in x_vals:
            g = ex.subgrad({'x':val})
            self.assertAlmostEqual(g['x'],2*val)


if __name__=='__main__':
    unittest.main()
