import unittest
import math
from subgradpy import *

class TestHuber(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_value(self):
        x = var('x')
        ex = huber(x,1.0);
        #Test for m=1, and for x values less than, -M, between -M and M,
        #and greater than M
        self.assertAlmostEqual(ex.get_value({'x': 1.0}),1)
        self.assertAlmostEqual(ex.get_value({'x':0.5}),0.5*0.5)
        self.assertAlmostEqual(ex.get_value({'x':-0.5}),0.5*0.5)
        self.assertAlmostEqual(ex.get_value({'x':100}),2*100-1)

        #Test for anoter M
        m=5.0
        ex2= huber(x,m)
        self.assertAlmostEqual(ex2.get_value({'x':-m}),m*m)
        self.assertAlmostEqual(ex2.get_value({'x':2}),4)
        self.assertAlmostEqual(ex2.get_value({'x':100}),2*m*100-m*m)

    def test_subgrad(self):
        m_vals = [1.0, 0.5, 5.0];
        x_vals = [-4,-1,0,1,5,100];
 
        for val in x_vals:
            for m in m_vals:
                x = var('x')
                ex = huber(x,m)
                g = ex.subgrad({'x':val})
                if math.fabs(val)<=m:
                    self.assertAlmostEqual(g['x'],2*val);
                else:
                    if val>0:
                        self.assertAlmostEqual(g['x'],2*m);   
                    else:
                        self.assertAlmostEqual(g['x'],-2*m);
        

if __name__=='__main__':
    unittest.main()
                                                     
    
    
