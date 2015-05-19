import math

def f(a,b,y):
    return (1 - ( a+b*y) * math.sin(2 * math.pi * y)) * math.exp( - y**2)
    
def numint(a, b, h):
    e = 1024
    
    #numerical integrate the result
    I = 0
    integral = 0
    while ( I < e):
        integral += h/e * f(a, b, I * h/e)** 2
        I +=1
    

    return integral
    
N = int(input())
I = 0
maxvol = 0
maxI = 0
while ( I < N):
    string = input()
    a = float(string.split()[0])
    b = float(string.split()[1])
    h = float(string.split()[2])
    vol = numint(a,b,h)
    if ( maxvol < vol):
        maxvol = vol
        maxI = I
    I +=1
    
print(str(maxI + 1))