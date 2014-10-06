from subgradpy.utils import *

class matrix(object):
    def __init__(self, m, n):
        self.nrow = m
        self.ncol = n
        self.data = [[0 for j in range(self.ncol)] for i in range(self.nrow)]
    def T(self): #transpose
        tnrow = self.ncol
        tncol = self.nrow
        ret = matrix(tnrow, tncol)
        ret.data = [[self.data[i][j] for i in range(tncol)] for j in range(tnrow)]
        return ret
    def __str__(self):
        return str(self.nrow) + '-by-' + str(self.ncol) + ' matrix: ' + str(self.data)

    def __setitem__(self, key, x):
        assert type(key) == tuple
        self.data[key[0]][key[1]] = x

    def __getitem__(self, key):
        assert type(key) == tuple
        return self.data[key[0]][key[1]]

    def __mul__(self, other):
        if isinstance(other, matrix):
            assert self.ncol == other.nrow
            ret = matrix(self.nrow, other.ncol)
            for i in range(ret.nrow):
                for j in range(ret.ncol):
                    v1 = self.data[i]
                    v2 = [other.data[k][j] for k in range(other.nrow)]
                    ret.data[i][j] = sum(v1[k]*v2[k] for k in range(len(v1)))
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, other.ncol)
            ret.data = [[other*self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, matrix):
            assert other.ncol == self.nrow
            ret = matrix(other.nrow, self.ncol)
            for i in range(ret.nrow):
                for j in range(ret.ncol):
                    v1 = other.data[i]
                    v2 = [self.data[k][j] for k in range(self.nrow)]
                    ret.data[i][j] = sum(v1[k]*v2[k] for k in range(len(v1)))
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, other.ncol)
            ret.data = [[other*self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented

    def __neg__(self):
        return (-1.0)*self

    def __add__(self, other):
        if isinstance(other, matrix):
            assert self.nrow == other.nrow
            assert self.ncol == other.ncol
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[self.data[i][j]+other.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[self.data[i][j]+other for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented
    def __radd__(self, other):
        if isinstance(other, matrix):
            assert self.nrow == other.nrow
            assert self.ncol == other.ncol
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[other.data[i][j]+self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[other+self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, matrix):
            assert self.nrow == other.nrow
            assert self.ncol == other.ncol
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[self.data[i][j]-other.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[self.data[i][j]-other for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, matrix):
            assert self.nrow == other.nrow
            assert self.ncol == other.ncol
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[other.data[i][j]-self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        elif isNumber(other):
            ret = matrix(self.nrow, self.ncol)
            ret.data[i][j] = [[other-self.data[i][j] for j in range(self.ncol)] for i in range(self.nrow)]
            return ret
        return NotImplemented

class vector(matrix):
    def __init__(self, n):
        matrix.__init__(self, n, 1)

    def __setitem__(self, i, x):
        assert isNumber(x)
        if self.nrow == 1: self.data[0][i] = x
        self.data[i][0] = x

    def __getitem__(self, i):
        if self.nrow == 1: return self.data[0][i]
        return self.data[i][0]

class matrix_var(matrix):
    def __init__(self, name, m, n):
        self.name = name
        self.nrow = m
        self.ncol = n
    def __str__(self):
        return self.name
    def get_value(self, varmap = {}):
        if self.name in varmap:
            return varmap[self.name]
        return NAN
    def get_vars(self):
        return set([self.name])
    def subgrad(self, varmap = {}): pass
    def supergrad(self, varmap = {}): pass
    def is_convex(self): return True
    def is_concave(self): return True

class vector_var(matrix_var):
    def __init(self, name, n):
        matrix_var.__init__(self, name, n, 1)
