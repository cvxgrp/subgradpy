import math
from subgradpy.scalar import *


class expr_rel_entr(object):
    """
    Relative entropy function: rel_entr(x,y)=x*log(x/y). 
    Convex (assuming x>0,y>0).
    For the case, y=1 the relative entropy function reduces to the negative entropy function.
    
    The relative entropy expression serves as an example of a function that
    is convex but violates the DCP ruleset (specifically, it violates the
    no-product rule).
    """

    def __init__(self):
        self.name = 'rel_entr'
    def __call__(self, *args):
        while type(args[0]) is list: args = args[0]
        assert len(args) == 2
        
        x = args[0]
        y = args[1]
        
        if isNumber(x) and isNumber(y):
            if x<=0 or y<=0:
                raise ValueError('relative entropy called with negative arguments x = %f , y = %f' % (x,y))
            print (x,y)
            return x*math.log(float(x)/y)
        if isNumber(x): x = scalar(x)
        if isNumber(y): y = scalar(y)
        return expr(self,[x,y])

    def subgrad(self, values):
        x = values[0]
        y = values[1]
        return [1.0+math.log(float(x)/y),-(x/y)]
    
    def is_increasing(self,argindex): False
    def is_decreasing(self,argindex): return argindex == 1
    def is_covex(self): return True
    def is_concave(self): return False

#Function instance
rel_entr = expr_rel_entr()
