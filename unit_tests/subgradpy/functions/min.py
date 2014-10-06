import __builtin__
from subgradpy.scalar import *

class expr_min(object):
    def __init__(self):
        self.name = 'min'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        
        x = args
        flag = False
        for xi in x:
            if isinstance(xi, expr):
                flag = True
                break
        if not flag: return __builtin__.min(x)
        y = []
        for i in range(len(x)):
            if isNumber(x[i]): y.append(scalar(x[i]))
            else: y.append(x[i])
        return expr(self, y)
        
    def supergrad(self, values):
        y = self(values)
        return [(float)(x == y) for x in values]
    def is_increasing(self, argindex): return True
    def is_decreasing(self, argindex): return False
    def is_convex(self): return False
    def is_concave(self): return True

# Function instance
min = expr_min()
