from subgradpy.scalar import *
import __builtin__


class expr_square_pos(object):
    """
    Square of max(0,x). square_pos = max{0,x}^2
    square_pos is non-decreasing, so it can accept a convex argument
 
    """
    def __init__(self):
        self.name = 'square_pos'
    def __call__(self,*args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 1
        
        x = args[0]
        if isinstance(x, expr):
            return expr(self,[x])
        else:
            return __builtin__.max(x,0)*__builtin__.max(x,0)
    def subgrad(self, values):
        x = values[0]
        return [2.0*__builtin__.max(x,0)]

    def is_increasing(self, argindex): return True
    def is_decreasing(self, argindex): return False
    def is_convex(self): return True
    def is_concave(self): return False

#Function instance
square_pos = expr_square_pos()
