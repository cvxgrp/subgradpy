import unittest
import math
from subgradpy import *

class testNorm1(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_value(self):
        x = var('x');
        y = var('y');
        z = var('z');
        var_map={'x':12.2,'y':-3.4,'z':0}
        ex = norm1(x,y,z)
        self.assertAlmostEqual(ex.get_value(var_map),
                               sum([math.fabs(elem) for elem in var_map.values()]))
    
    def test_subgrad(self):
        x = var('x');
        y = var('y');
        z = var('z');
        var_map={'x':12.2,'y':-3.4,'z':0}
        ex = norm1(x,y,z)
        g = ex.subgrad(var_map)
        self.assertEqual(g['x'],1.0)
        self.assertEqual(g['y'],-1.0)
        self.assertTrue(math.fabs(g['z'])<=1.0)
        

if __name__=='__main__':
    unittest.main()
