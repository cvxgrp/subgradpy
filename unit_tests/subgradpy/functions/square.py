from subgradpy.scalar import *

class expr_square(object):
    def __init__(self):
        self.name = 'square'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 1
        
        x = args[0]
        if isinstance(x, expr):
            return expr(self, [x])
        else:
            return x*x
    def subgrad(self, values):
        x = values[0]
        return [2.0*x]
    def is_increasing(self, argindex): return False
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

# Function instance
square = expr_square()
