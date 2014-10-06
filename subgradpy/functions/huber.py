import math
from subgradpy.scalar import *
from subgradpy.utils import *

class expr_huber(object):
    def __init__(self):
        self.name = 'huber'
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
            return x*x
        else:
            return M*(2.0*math.fabs(x)-M)
    def subgrad(self, values):
        x = values[0]
        M = values[1]
        if math.fabs(x) <= M: return [2.0*x, 0.0]
        elif x > M: return [2.0*M, 2.0*(x-M)]
        elif x < -M: return [-2.0*M, 2.0*(-x-M)]
    def is_increasing(self, argindex): return argindex == 1
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
huber = expr_huber()
