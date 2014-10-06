import math
from subgradpy.scalar import *

class expr_log(object):
    def __init__(self):
        self.name = 'log'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 1
        
        x = args[0]
        if isinstance(x, expr):
            return expr(self, [x])
        elif x <= 0:
            raise ValueError('log called with negative argument %f' %x)
        else:
            return math.log(x)
    def supergrad(self, values):
        x = values[0]
        if x <= 0.0:
            raise ValueError('log called with negative argument %f' %x)
        else:
            return [1.0/x]
    def is_increasing(self, argindex): return True
    def is_decreasing(self, argindex): return False
    def is_convex(self): return False
    def is_concave(self): return True

# Function instance
log = expr_log()
