import math
import random
from subgradpy.scalar import *
from subgradpy.utils import *

class expr_berhu(object):
    def __init__(self):
        self.name = 'berhu'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 1 or len(args) == 2
        if len(args) == 1: args.append(1.0)        
        assert isNumber(args[1]) and args[1] >= 0
        
        x = args[0]
        M = args[1]
        if isinstance(x, expr):
            return expr(self, [x, scalar(M)])
        elif math.fabs(x) <= M:
            return math.fabs(x)
        else:
            return (x*x+M*M)/(2.0*M)
    def subgrad(self, values):
        x = values[0]
        M = values[1]
        if x == 0.0: return [random.uniform(-1.0, 1.0), 0.0]
        elif 0.0 < x <= M:  return [1.0, 0.0]
        elif -M <= x < 0.0: return [-1.0, 0.0]
        return [x/M, 1.0-(x*x+M*M)/(2.0*M*M)]
    def is_increasing(self, argindex): return False
    def is_decreasing(self, argindex): return argindex == 1
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
berhu = expr_berhu()
