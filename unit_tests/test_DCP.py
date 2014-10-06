import unittest
import math
from subgradpy import *

class TestDCP(unittest.TestCase):
    def setUp(self):
        pass



    def test_affine(self):
        x = var ('x')
        a = 3;
        b = -2;
        leq(a*x+b,0)
        pass

    def test_sum(self):
        x = var ('x')
        y = var ('y')
        leq(x+y,0)
        pass

    def test_exp(self):#e^(ax)
        x = var ('x')
        a = 3
        leq(exp(3*x),0)
        pass
    
    

    def test_square(self):#square(affine argument) is convex
        x = var ('x')
        y = var ('y')
        leq(square(x+y),0)
        self.assertRaises(AssertionError,leq,square(square(x+y)),0)#not DCP convex
        #use square_pos instead
        leq(square_pos(square(x+y)),0)

    def test_max(self):
        x = var ('x')
        y = var ('y')
        leq(max(3*x+y,square(y)),0)
        leq(-min(max(x,y),4*x),0)
        
    def test_quad_over_linear(self):#(x+y)^2/sqrt(y)
        x = var ('x')
        y = var ('y')
        #self.assertRaises(AssertionError,leq,square(x+y)/sqrt(y)),0)
        leq(quad_over_lin(square(x+y),sqrt(y)),0)

    def test_log_sum_exp(self):
        x = var('x')
        y = var('y')
        z = var('z')
        leq(log_sum_exp(x,0)-x,0)
        leq(max(log_sum_exp(x,y,z),log_sum_exp(x,y)),0)

    def test_non_convex(self):
        x = var('x')
        y = var('y')
        self.assertRaises(AssertionError, leq, exp(log(x)),0)
        self.assertRaises(AssertionError, leq, 1-exp(x),0);
        self.assertRaises(AssertionError, leq, sqrt(2*x+y),0)
        self.assertRaises(AssertionError, leq, quad_over_lin(sqrt(x),y),0)
        #self.assertRaises(AssertionError, leq, power(x,3),0)
if __name__=='__main__':
    unittest.main()
