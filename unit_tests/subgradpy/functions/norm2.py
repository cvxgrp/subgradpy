import math
from subgradpy.utils import *
from subgradpy.scalar import *

class expr_norm2(object):
    def __init__(self):
        self.name = 'norm2'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        
        x = args
        flag = False
        for xi in x:
            if isinstance(xi, expr):
                flag = True
                break
        if not flag: return math.sqrt(sum([xi**2.0 for xi in x]))
        y = []
        for i in range(len(x)):
            if isNumber(x[i]): y.append(scalar(x[i]))
            else: y.append(x[i])
        return expr(self, y)
            
    def subgrad(self, values):
        val = self(values)
        return [x/val for x in values]
    def is_increasing(self, argindex): return False
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
norm2 = expr_norm2()
