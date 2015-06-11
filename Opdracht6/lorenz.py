from numpy import array
from scipy.integrate import odeint
from scipy.linalg import eigvals
class Lorenz():
    
    __slots__ = { "_x", "_y", "_z", "_sigma", "_rho", "_beta"}
    
    def __init__(self, vars,sigma = 10, rho =28, beta = 8.0/3):
        self._x = vars[0]
        self._y = vars[1]
        self._z = vars[2]
        self._sigma = sigma
        self._rho = rho
        self._beta = beta
        
    def F(self, vec, _):
        xt = vec[0]
        yt = vec[1]
        zt = vec[2]
        dotx = self._sigma * (yt - xt)
        doty = xt * (self._rho - zt) - yt
        dotz = xt * yt - self._beta * zt
        return array([dotx, doty, dotz])
        
    def df(self, vec, _):
        xt = vec[0]
        yt = vec[1]
        zt = vec[2]
        
        dx = [- self._sigma, self._sigma, 0]
        dy = [self._rho - zt - yt, -1, - xt]
        dz = [yt, xt, self._beta]
        gradient = array([dx, dy, dz])
        return gradient
        
    def solve(self, T, dt):
        
        vec = array ([self._x, self._y, self._z])
        timevec = []
        t = 0
        while ( t < T):
            timevec.append(t)
            t += dt
        timevec.append(T)

        return odeint(self.F, vec, timevec, (), self.df)
    
    def isStable(self, vec):
        eigs = eigvals(self.df(vec, 0))
        i = 0
        while ( i < 3):
            if (eigs[i].real >= 0):
                return False
            i+=1
        
        return True
        
        