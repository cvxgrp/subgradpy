import math
from subgradpy.scalar import *

class expr_exp(object):
    def __init__(self):
        self.name = 'exp'
    def __call__(self, *args):
        if len(args) != 1:
            raise ValueError('exp called with multiple arguments')
        
        if type(args[0]) is list:
            x = args[0][0]
        else:
            x = args[0]
        
        if isinstance(x, expr):
            return expr(self, [x])
        else:
            return math.exp(x)
    def subgrad(self, values):
        x = values[0]
        return [self(x)]
    def is_increasing(self, argindex): return True
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
exp = expr_exp()
