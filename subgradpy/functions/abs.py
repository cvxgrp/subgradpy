import math
import random
from subgradpy.scalar import expr

class expr_abs(object):
    def __init__(self):
        self.name = 'abs'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 1
        
        x = args[0]
        if isinstance(x, expr):
            return expr(self, [x])
        return math.fabs(x)
    def subgrad(self, values):
        x = values[0]
        if x > 0.0:   return [1.0]
        elif x < 0.0: return [-1.0]
        else:         return [random.uniform(-1.0, 1.0)]
    def is_increasing(self, argindex): return False
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
abs = expr_abs()
