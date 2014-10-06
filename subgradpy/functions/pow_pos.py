import math
from subgradpy.scalar import *

class expr_pow_pos(object):
    """
    Function pos_pos(x,p) = max(x,0)^p where p is a constant>=1 (same as
    in CVX)
     Convex and non-decreasing.
     """
    def __init__(self):
        self.name = 'pow_pos'
        
    def __call__(self,*args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 2
        
        x = args[0]
        p = args[1]
        
        if p == 0: return 1;
        if p == 1: return x;
        
        if isinstance(x,expr):
            return expr(self,[x, scalar(p)])
        else:
            if p<1:
                raise ValueError('pow_pos called with exponent %f <1' %p)
            else:
                return pow(max(x,0),p)

    def subgrad(self, values):
        x = values[0]
        p = values[1]
        if x<=0: 
            return 0.0
        else:
            return [p*pow(x,p-1)]

    def is_increasing(self, argindex): True
    def is_decreasing(self, argindex): pass
    def is_convex(self): True
    def is_concave(self): pass
        
# Function instance
pow_pos = expr_pow_pos()
