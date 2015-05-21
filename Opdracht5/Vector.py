import math
from array import array

class Vector():
    
    __slots__ = {"_N" , "_vec"}
    
    def __init__(self, n = 1 , vect = None):
        self._N = n
        try:
            if vect == None:
                self._vec = array('d', [0]*n)
            elif len(vect) == n:
                self._vec = array('d', vect)
            else:
                self._vec = array('d', [0]* n)
        except:
            self._vec = array('d', [vect] * n)
        
    def __add__(self, other):
        if (isinstance(other, Vector) == False):
            raise Exception("Cannot add vector with Other type")
        if (self._N != other._N):
            raise Exception("Adding vectors of different length")
        w = array('d', [0]* self._N)
        for i in range(self._N):
            w[i] = self._vec[i] + other._vec[i]
        self._vec = w
        return self
    
    def __sub__(self, other):
        if (isinstance(other, Vector) == False):
            raise Exception("Cannot subtract vector with Other type")
        if (self._N != other._N):
            raise Exception("Subtracting vectors of different length")
        w = array('d', [0]* self._N)
        for i in range(self._N):
            w[i] = self._vec[i] - other._vec[i]
        self._vec = w
        return self

    def __rmul__(self, other):
        for i in range(self._N):
            self._vec[i] = self._vec[i] * other
        return self
    
    def __str__(self):
        prut = ""
        for i in range(self._N - 1):
            prut += str(self._vec[i]) + "\n"
        prut += str(self._vec[self._N -1])
        return prut
    
    def inner(self, other):
        
        prod = 0.0
        for i in range(self._N):
            prod += self._vec[i] * other._vec[i]
        return prod
    
    def norm(self):
        return math.sqrt(self.inner(self))
        
    def scalar(self, alpha):
        return alpha * self
    
    def lincomb(self, other, alpha, beta):
        return alpha * self + beta * other
    
    def Clone(self):
        return Vector(self._N, self._vec)
        
def GrammSchmidt(vecs):
    res = [ 1/vecs[0].norm() * vecs[0].Clone() ]
    i = 1
    while ( i < len(vecs)):
        vec = step = vecs[i].Clone()
        j = 0
        while ( j < i):
            vec2 = res[j].Clone()
            proj = vec.inner(vec2) / vec2.inner(vec2) * vec2 # the project on the jth coord
            step = step - proj #remove this projection
            j+=1
        res.append(1/step.norm() * step)

        i+=1
    return res