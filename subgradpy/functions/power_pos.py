import math
import __builtin__
from subgradpy.scalar import *

class expr_power_pos(object):
    """
    Function power_pos(p,x) = max {0 ,p} ^ x, where x>=1.
   
    """
    def __init__(self):
        self.name = 'power_pos'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 2
        
        p = args[0]
        x = args[1]


  
        if p == 0 or p == 1:
            return p
        elif 0 < p < 1:
            if isinstance(x, expr):
                return expr(self, [scalar(p), x])
            else:
                if x<1:
                    raise ValueError('power_pos called with exponent %f < 1' %x)
                return pow(max(p,0), x)
        elif p > 1:
            if isinstance(x, expr):
                return expr(self, [scalar(p), x])
            else:
                if x<1:
                    raise ValueError('power_pos called with exponent %f < 1' %x)
                return pow(max(0,p), x)
        else:
            raise ValueError('power called with negative base %f' %p)

    def subgrad(self, values):
        p = values[0]
        x = values[1]
        base = max(0,p)
        if base == 0.0 or base == 1.0: return [0.0]
        else:                          return [pow(base, x)*math.log(base)]
    def is_increasing(self, argindex): pass
    def is_decreasing(self, argindex): pass
    def is_convex(self): pass
    def is_concave(self): pass

# Function instance
power_pos = expr_power_pos()
