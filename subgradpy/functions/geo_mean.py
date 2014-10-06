import math
import __builtin__
from subgradpy.scalar import *

class expr_geo_mean(object):
    """
    Geometric Mean of a vector (represented as a list)  
    geom_mean(x_1,...,x_n)=(x_1*...*x_n)^(1/n)
    Assume all entries x_i are non-negative.
    Concave and increasing.

    """
    def __init__(self):
        self.name = 'geo_mean'
    def __call__(self,*args):
        while type(args[0]) is list: args = args[0]
        
        x = args
        n = float(len(args))
        
        flag = False
        for xi in x:
            if isinstance(xi, expr):
                flag = True 
                break
        if not flag: 
            for xi in x:
                if xi == 0: return 0
                if xi < 0: raise ValueError('geometric mean called with'
                                            'a vector containing a negative entry')
            
                return math.exp(sum([math.log(xi)/n for xi in x]))
        y = []
        for i in range(len(x)):
            if isNumber(x[i]): y.append(scalar(x[i]))
            else: y.append(x[i])
        return expr(self, y)


    def subgrad(self, values):
        n = float(len(values))
        prod = math.exp(sum([math.log(xi)/n for xi in values]))
        return [prod/(xi*n) for xi in values]

    def is_increasing(self, argindex): return True
    def is_decreasing(self, argindex): return False
    def is_convex(self): return False
    def is_concave(self): return True

# Function instance
geo_mean = expr_geo_mean()
