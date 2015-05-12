
def findroot(f, a, b, e):
    m = (a + b)/2
    #check if we are done
    if abs(b-a)< e:
        return m
    if f(m) == 0:
        return m
    #we are not done, check to verify if there is a root in the first halve
    if (f(a) * f(m) < 0):
        #we will find a root in this interval
        return findroot(f, a, m, e)
    #check to verify if there is a root in the first value
    elif (f(b) * f(m) < 0):
        return findroot(f, m, b, e)

def findroot2(f,a,b,e):

    m = (a + b)/2
    #check if we are done
    if abs(b-a)< e:
        if (abs(f(m))>0.00001):
            return a - 2* b
        return m
    if f(m) == 0:
        return m
    
    #we are not done, check to verify if there is a root in the first halve
    if (f(a) * f(m) < 0):
        #we will find a root in this interval
        return findroot2(f, a, m, e)
    #check to verify if there is a root in the first value
    elif (f(b) * f(m) < 0):
        return findroot2(f, m, b, e)
    
    #now we have yet to find a root 
    res = findroot2(f,a, m, e)
    if (res == a - 2*m):
        
        res = findroot2(f,a,m, e)
        if (res == m - 2*b):
            return a - 2*b
        else:
            return res
    else:
        return res

def findallroots(f,a,b,e):
    ls = []
    if e == 0:
        return
    if ( b < a):
        t = b
        b = a
        a = t
    #blijf ophogen tot een teken flip gevonden wordt
    while (a <b):
        if (f(a) * f(a + e) < 0):
            ls.append(a + 0/5 * e)
        a += e
    return ls