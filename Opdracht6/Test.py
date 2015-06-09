from Lorenz import Lorenz
from numpy import array
import math
sigma = 10.0
rho = 28.0
beta = 8.0/3

L1 = Lorenz([-1, 1, 0], sigma, rho, beta)
u1 = L1.solve(50,0.01)

L2 = Lorenz([-1.001,1.001,0.001],sigma,rho,beta)
u2 = L2.solve(50, 0.01)

L3 = Lorenz(array([math.sqrt(beta * ( rho - 1)), math.sqrt(beta * (rho -1)), rho -1]), sigma, rho, beta)
print(L3.isStable(array([math.sqrt(beta * ( rho - 1)), math.sqrt(beta * (rho -1)), rho -1])))

j = 0
while ( j < 3):
    print(u1[0,j], u2[0,j])
    j += 1
print(u1[-1,0], u2[-1,0])

print("klaar")