i = 1
smallestprod = 1
while ( i <= 20):
    smallestprodnew = smallestprod
    while (smallestprodnew % i != 0):
        smallestprodnew += smallestprod
    smallestprod = smallestprodnew
    i+=1
print smallestprod    