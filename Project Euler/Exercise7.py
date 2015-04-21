import math

#A sped up isprime function
def isprime(n):
    
    #try for div by 2
    if (n% 2 == 0) and (n != 2):
        return False
        
    #try for div by 3
    if (n% 3 == 0) and (n!= 2):
        return False
        
    #try for div by 5
    if (n % 5 == 0) and (n != 5):
        return False
    
    i = 1
    sq = math.sqrt(n)
    while (i <= sq):
        if (n % (i * 6 + 1) == 0) and ( n != i * 6 + 1):
            return False
        if (n % (i * 6 + 5) == 0) and ( n != i * 6 + 5):
            return False
        i+=1
    return True
    
i  = 1
j = 0
while (j< 10001):
    if isprime(i):
        j += 1
    i+=1

print i - 1