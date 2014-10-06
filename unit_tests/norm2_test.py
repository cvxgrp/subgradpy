import unittest
import math
from subgradpy import *

class testNorm2(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_value(self):
        x = var('x');
        y = var('y');
        z = var('z');
        var_map={'x':12.2,'y':-3.4,'z':0.0}
        ex = norm2(x,y,z)
        self.assertAlmostEqual(ex.get_value(var_map),
                               math.sqrt(sum([elem*elem for elem in var_map.values()])))
    
    def test_subgrad(self):
        x = var('x');
        y = var('y');
        z = var('z');
        var_map={'x':12.2,'y':-3.4,'z':0}
        ex = norm2(x,y,z)
        g = ex.subgrad(var_map)
        self.assertAlmostEqual(g['x'],12.2/(math.sqrt(12.2**2.0+3.4**2.0)))
        self.assertAlmostEqual(g['y'],-3.4/(math.sqrt(12.2**2.0+3.4**2.0)))
        self.assertAlmostEqual(g['z'],0)

        

if __name__=='__main__':
    unittest.main()
