import sys
import random
import math


def drop_needle(L, R):
    x = R.random()
    a = R.vonmisesvariate(0,0)
    xeind = x + L * math.cos(a)
    
    if (xeind < 0) or (xeind > 1):
        return True
    return False
    
if True:
    if (len(sys.argv) < 3):
        print("Use: python estimate_pi.py N L")
    else:
        N = int(sys.argv[1])
        L = float(sys.argv[2])
        if (L > 1):
            print("AssertionError: L should be smaller than 1")
        else:
            i = 0
            count = 0
            R = random
            if (len(sys.argv) == 4):
                seed = int(sys.argv[3])
                R.seed(seed)
            while (i< N):
                if drop_needle(L, R):
                    count += 1
                i+=1
            
            print(str(count) + " hits in " + str(N) + " tries")
            print("Pi = " + str(2 * L * N / count))
    