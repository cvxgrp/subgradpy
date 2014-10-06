import unittest
import math
from subgradpy import *


class testSqrt(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_value(self):
        x = var('x')
        ex = sqrt(x);
        x_vals = [-3.14 ,-0.0 ,123.1]
        for x_val in x_vals:
            try:
                ex_val = ex.get_value({'x':x_val})
                self.assertAlmostEqual(ex_val,math.sqrt(x_val))
            except ValueError:
                print 'sqrt of negative number. Exception caught'
                
    def test_supergrad(self):
        x = var('x')
        ex = sqrt(x);
        g = ex.supergrad({'x':123.456}) 
        self.assertAlmostEqual(g['x'],0.5/sqrt(123.456))

if __name__=='__main__':
    unittest.main()
