import math
from scalar import *
from constraint import *
from functions import *

class problem(object):
    def __init__(self, type, obj, constraints):
        if isNumber(obj): obj = scalar(obj)
        assert type in [MINIMIZE, MAXIMIZE]
        assert (type == MINIMIZE and obj.is_convex()) or (type == MAXIMIZE and obj.is_concave())
        self.type = type
        self.obj = obj
        self.constraints = []
        for cons in constraints:
            if cons.relop == LT or cons.relop == EQ:
                self.constraints.append(cons.lhs-cons.rhs)
            if cons.relop == GT or cons.relop == EQ:
                self.constraints.append(cons.rhs-cons.lhs)
        
    def solve(self, stepsize = 1.0/scalar_var('iter'), cur = None):
        if isNumber(stepsize): stepsize = scalar(stepsize)
        if self.type == MAXIMIZE:
            self.obj = -self.obj
        vars = self.obj.get_vars()
        if cur == None:
            cur = {}
            for var in vars: cur[var] = 0.0
        optval = None
        for iter in range(1, MAXITERS+1):
            f = self.obj.get_value(cur)
            g = None
            maxres = 0
            for cons in self.constraints:
                if cons.get_value(cur) > maxres:
                    maxres = cons.get_value(cur)
                    g = cons.subgrad(cur)
            if g == None: g = self.obj.subgrad(cur)
            norm = math.sqrt(sum([x**2 for x in g.itervalues()]))
            if norm < EPS: break
            nxt = {}
            if self.type == MAXIMIZE:
                stepsizedic = {'f': -f, 'gnorm': norm, 'iter': iter}
            else:
                stepsizedic = {'f': f, 'gnorm': norm, 'iter': iter}
            alpha = stepsize.get_value(stepsizedic)
            assert alpha > 0
            for (key, val) in g.iteritems():
                nxt[key] = cur[key]-val*alpha
            cur = nxt
        if self.type == MAXIMIZE:
            self.obj = -self.obj
        optval = self.obj.get_value(cur)
        return (optval, cur)
    
    # def kelley(self, initpoint):
        # constraints = []
        # for cons in self.constraints:
            # assert cons.get_value(initpoint) <= 0
            # constraints.append(constraint(cons, LT, 0))
        
        # if self.type == MAXIMIZE:
            # self.obj = -self.obj

        # kelleyobj = 0
        # cur = initpoint
        # u = self.obj.get_value(cur)
        # optpoint = cur
        # cuttingplanes = []
        # for iter in range(1, KELLEYITERS+1):
            # f = self.obj.get_value(cur)
            # if u > f:
                # u = f
                # optpoint = cur
            # g = self.obj.subgrad(cur)
            # vars = self.obj.get_vars()
            # t = f
            # for varname in vars:
                # varexpr = scalar_var(varname)
                # t = t+g[varname]*(varexpr-cur[varname])
            # cuttingplanes.append(t)
            # (l, cur) = problem(MINIMIZE, max(cuttingplanes), constraints).solve(cur)

        # if self.type == MAXIMIZE:
            # self.obj = -self.obj

        # optval = self.obj.get_value(optpoint)
        # return (optval, optpoint)
