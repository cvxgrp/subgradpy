import random
import math
from subgradpy.utils import *
from subgradpy.scalar import *

class expr_norm1(object):
    def __init__(self):
        self.name = 'norm1'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        
        x = args
        flag = False
        for xi in x:
            if isinstance(xi, expr):
                flag = True
                break
        if not flag: return sum([math.fabs(xi) for xi in x])
        y = []
        for i in range(len(x)):
            if isNumber(x[i]): y.append(scalar(x[i]))
            else: y.append(x[i])
        return expr(self, y)
            
    def subgrad(self, values):
        ret = []
        for x in values:
            if   x > 0.0: ret.append(1.0)
            elif x < 0.0: ret.append(-1.0)
            else:         ret.append(random.uniform(-1.0, 1.0))
        return ret
    def is_increasing(self, argindex): return False
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
norm1 = expr_norm1()
