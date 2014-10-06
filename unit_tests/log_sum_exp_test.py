import unittest
import math
from subgradpy import *

class testLSE(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_value(self):
        x = var('x')
        ex = log_sum_exp(x);
        x_vals=[-3,5,0,1,10];
        self.assertAlmostEqual(ex.get_value({'x': x_vals}),math.log(sum([exp(xi) for xi in x_vals])))
        
    def test_subgrad(self):
        x = var('x');
        y = var('y');
        z = var('z');
        ex = log_sum_exp(x,y,z);
        x_val = -4.2
        y_val = -0.0
        z_val = 3.5
        g = ex.subgrad({'x':x_val,'y':y_val,'z':z_val})
        expsum=math.exp(x_val)+math.exp(y_val)+math.exp(z_val);
        self.assertAlmostEqual(g['x'],exp(x_val)/expsum)
        self.assertAlmostEqual(g['y'],exp(y_val)/expsum)
        self.assertAlmostEqual(g['z'],exp(z_val)/expsum)

if __name__=='__main__':
    unittest.main()
