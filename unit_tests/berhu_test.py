import unittest
import math
from subgradpy import *

class TestBerhu(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_value(self):
        x = var('x')
        ex = berhu(x,1.0);
        #Test for m=1, and for x values less than, -M, between -M and M,
        #and greater than M
        self.assertAlmostEqual(ex.get_value({'x': 1.0}),1)
        self.assertAlmostEqual(ex.get_value({'x':0.5}),0.5)
        self.assertAlmostEqual(ex.get_value({'x':-0.5}),0.5)
        self.assertAlmostEqual(ex.get_value({'x':10}),(10*10+1.0)/2.0)

        #Test for anoter M
        m=5.0
        ex2= berhu(x,m)
        self.assertAlmostEqual(ex2.get_value({'x':-m}),m)
        self.assertAlmostEqual(ex2.get_value({'x':2}),2)
        self.assertAlmostEqual(ex2.get_value({'x':10}),(100.0+m*m)/(2*m))

    def test_subgrad(self):
        m_vals = [1.0, 0.5, 5.0];
        x_vals = [-5,-1,0,1,5,100];
        for val in x_vals:
            for m in m_vals:
                x = var('x')
                ex = berhu(x,m)
                g = ex.subgrad({'x':val})
                if val==0: 
                    self.assertTrue(g['x']<=1)
                    self.assertTrue(g['x']>=-1)
                elif math.fabs(val)<=m:
                    if val>0:
                        self.assertAlmostEqual(g['x'],1.0) 
                    else:
                        self.assertAlmostEqual(g['x'],-1.0)
                else:                   
                    self.assertAlmostEqual(g['x'],1.0*val/m);
     

if __name__=='__main__':
    unittest.main()
