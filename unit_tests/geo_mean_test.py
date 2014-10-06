import unittest
import math
from subgradpy import *

class TestGeoMean(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_value(self):
        x = var ('x')
        y = var ('y')
        z = var ('z')
        ex1 = geo_mean(x,y)
        self.assertAlmostEqual(ex1.get_value({'x':2,'y':8}),4)
        ex2 = geo_mean(x)
        self.assertAlmostEqual(ex2.get_value({'x':123}),123)
        ex3 = geo_mean(x,y,z)
        self.assertAlmostEqual(ex3.get_value({'x':4,'y':8, 'z':2}),4)
    
    def test_supergrad(self):
        x = var ('x');
        y = var ('y');
        z = var ('z');
        ex1 = geo_mean(x,y)
        g1 = ex1.supergrad({'x':3.0,'y':100.0})
        self.assertAlmostEqual(g1['x'],0.5*math.sqrt(100.0/3.0))
        self.assertAlmostEqual(g1['y'],0.5*math.sqrt(3.0/100.0))

if __name__=='__main__':
    unittest.main()
