import math
from subgradpy.scalar import *

class expr_quad_over_lin(object):
    def __init__(self):
        self.name = 'quad_over_lin'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 2
        
        x = args[0]
        y = args[1]
        if isNumber(x) and isNumber(y):
            if y==0: raise ValueError('Division by zero in quadratic over linear')
            return x*x/y
        if isNumber(x): x = scalar(x)
        if isNumber(y): y = scalar(y)
        return expr(self, [x, y])
        
    def subgrad(self, values):
        x = values[0]
        y = values[1]
        return [2*x/y, -(x*x)/(y*y)]
    def is_increasing(self, argindex): return argindex == 0
    def is_decreasing(self, argindex): return argindex == 1
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
quad_over_lin = expr_quad_over_lin()
