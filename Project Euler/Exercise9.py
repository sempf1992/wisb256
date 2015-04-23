a = 1
while ( a < 1000):
    b = a
    while (b < 1000):
        c = 1000 - a - b
        if ( a**2 + b**2 == c**2):
            print(a*b*c)
        b+=1
    a+=1