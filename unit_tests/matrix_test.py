#!/usr/bin/env python

from subgradpy import *
if __name__ == "__main__":
    A = matrix(3, 4)
    x = vector(4)
    y = vector(3)
    aa = [[1, 2, 3, 5], [0, 2, -3, 1], [-1.5, 3.14, 2.718, 0.0]]
    xx = [5, -3, 1.0, 2.222]
    yy = [-1, 5, 234]
    for i in range(3):
        for j in range(4): A[i, j] = aa[i][j]
    for i in range(4): x[i] = xx[i]
    for j in range(3): y[j] = yy[j]
    print A
    print x
    print A*x
    print y.T()*A
    print y.T()*A*x
    