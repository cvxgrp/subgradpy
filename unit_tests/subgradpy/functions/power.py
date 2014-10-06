import math
from subgradpy.scalar import *

class expr_power(object):
    def __init__(self):
        self.name = 'power'
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
                return pow(p, x)
        elif p > 1:
            if isinstance(x, expr):
                return expr(self, [scalar(p), x])
            else:
                return pow(p, x)
        else:
            raise ValueError('power called with negative base %f' %p)

    def subgrad(self, values):
        p = values[0]
        x = values[1]
        if p == 0.0 or p == 1.0: return [0.0]
        else:                    return [pow(p, x)*math.log(p)]
    def is_increasing(self, argindex): pass
    def is_decreasing(self, argindex): pass
    def is_convex(self): pass
    def is_concave(self): pass

# Function instance
power = expr_power()
