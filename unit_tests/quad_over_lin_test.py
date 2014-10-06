import unittest
import math
from subgradpy import *

class testQOL(unittest.TestCase):
    def setUp(self):
        pass
    

    def test_get_value(self):
        x = var('x');
        y = var('y');
        ex = quad_over_lin(x,y)
        var_map = {'x':123.2, 'y':-2.3}
        self.assertAlmostEqual(ex.get_value(var_map),123.2**2.0/-2.3)

    def test_div_by_zero(self):
        x = var('x');
        y = var('y');
        ex = quad_over_lin(x,y)
        var_map = {'x':123.2, 'y':0}
        try:
            ex.get_value(var_map)
            
        except ValueError:
            print 'Division by zero error caught'
            pass
      
        #self.assertRaises(ValueError,ex.get_value(var_map))

    def test_subgrad(self):
        x = var('x');
        y = var('y');
        ex = quad_over_lin(x,y)
        var_map = {'x':123.2, 'y':-2.3}
        g = ex.subgrad(var_map)
        self.assertAlmostEqual(g['x'],2.0*var_map['x']/var_map['y'])
        self.assertAlmostEqual(g['y'],-var_map['x']**2.0/var_map['y']**2.0)



if __name__=='__main__':
    unittest.main()
