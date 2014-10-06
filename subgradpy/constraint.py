from subgradpy.constants import *
from subgradpy.scalar import *
from subgradpy.utils import *

class constraint(object):
    def __init__(self, lhs, relop, rhs):
        assert relop in [EQ, LT, GT]
        if isNumber(lhs): lhs = scalar(lhs)
        if isNumber(rhs): rhs = scalar(rhs)
        if relop == EQ:
            assert lhs.is_affine() and rhs.is_affine()
        if relop == LT:
            assert lhs.is_convex() and rhs.is_concave()
        if relop == GT:
            assert lhs.is_concave() and rhs.is_convex()
        self.lhs = lhs
        self.rhs = rhs
        self.relop = relop
    def cutting_plane(self, varmap = {}):
        g = (self.lhs-self.rhs).subgrad(varmap)
        vars = self.obj.get_vars()
        t = 0
        for varname in vars:
            varexpr = scalar_var(varname)
            t = t+g[varname]*(varexpr-cur[varname])
        return constraint(t, LT, 0)
