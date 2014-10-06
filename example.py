#!/usr/bin/env python

"""Example: Declaring Expressions and Retrieving Subgradients"""

from subgradpy import *


def example_expressions():
    x = var('x')
    y = var('y')
    
    ex = x+3
    print ex
    ex = 3+x
    print ex
    
    ex = exp(x+y)
    print ex.get_vars()
    print ex.get_value()
    print ex.get_value({'x': 2, 'y': -1})
    print ex.get_value({'x': 2})
    
    ex = exp(x)
    print ex
    print 'computing subgrad at x=2, y=-1'
    print ex.subgrad({'x': 2, 'y': -1})
    
    ex = exp(exp(x))
    print ex
    print ex.get_value({'x': 1})
    print ex.get_value({'x': 0})
    print ex.subgrad({'x': 0})
    
    ex = max(x, y)
    print ex
    print ex.get_value({'x': 1124, 'y': 233})
    print ex.subgrad({'x': 1124, 'y': 233})
    
    ex = 3*x+y*4
    print ex
    print ex.get_value({'x': 1124, 'y': 233})
    print ex.subgrad({'x': 1124, 'y': 233})
    
    ex = sqrt(x+y)
    print ex
    print ex.get_value({'x': 3, 'y': 4})
    print ex.supergrad({'x': 3, 'y': 4})

    ex = max(0, 3*x)
    print ex
    print ex.subgrad({'x': 123})
    
    ex = 3*x
    print ex
    print ex.subgrad({'x': 123})
	
    ex = abs(x-3)+exp(x)
    print ex
    print ex.subgrad({'y': -2})
    
    ex = abs(-3+x-3)+exp(x)
    print ex
    print ex.subgrad({'y': -2})
    
    ex = x+3
    print ex
    print ex.get_value({'x': 12345})
    print ex.subgrad({'x': 12345})

    ex = geo_mean(x,y)
    print ex
    print ex.get_value({'x':2,'y':8})
    print ex.subgrad({'x':1,'y':100})

    ex = square_pos(x)
    print ex.get_value({'x':2})
    print ex.get_value({'x':-5})
    print ex.subgrad({'x':1})
    
    ex = rel_entr(x,y)
    print ex
    print ex.get_value({'x':2.0,'y':8.0})
    print ex.subgrad({'x':1,'y':100})

    ex = pow_pos(x,5.0)
    print ex
    print ex.get_value({'x': 2.0})
    print ex.get_value({'x': -2.0})
    print ex.subgrad({'x':2.0})



def print_sol(arg):
    (optval, optpoint) = arg
    print 'objective value: ' + str(optval)
    print 'optimal point: '
    for key, val in optpoint.iteritems():
        print key + ': ' + str(val)

def example_problem():
    x1 = var("x1")
    x2 = var("x2")
    
    ex1 = x1+x2
    ex2 = -x1-x2
    ex3 = x1
    ex4 = max(x1, x2)
    ex5 = square(x1)+9*square(x2)
    
    constraints = [geq(2*x1+x2, 1), geq(x1+3*x2, 1), geq(x1, 0), geq(x2, 0)]

    print_sol(minimize(ex1, constraints).solve())
    print_sol(minimize(ex2, constraints).solve())
    print_sol(minimize(ex3, constraints).solve())
    print_sol(minimize(ex4, constraints).solve())
    print_sol(minimize(ex5, constraints).solve())
    
    print_sol(maximize(-ex1, constraints).solve())
    print_sol(maximize(-ex2, constraints).solve())
    print_sol(maximize(-ex3, constraints).solve())
    print_sol(maximize(-ex4, constraints).solve())
    print_sol(maximize(-ex5, constraints).solve())


if __name__ == "__main__":
    example_expressions()
    example_problem()
