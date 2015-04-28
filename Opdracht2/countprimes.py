#import important information
import sys
import math

C = 0.6601618
prev = -1
count1 = 0
count2 = 0
#try:
if True:
    with open(sys.argv[1], "r") as f:
        for line in f:
            #add count for a prime
            count1 +=1
            
            #see if it is a twin prime
            if (int(line) -2 == prev):
                count2+=1
            prev = int(line)
    
    print("Largest Prime =  " + str(prev))
    print("--------------------------------")
    print("pi(N)         =  " + str(count1))
    print("N/log(N)      =  " + str(prev/math.log(prev)))
    print("ratio         =  " + str(count1 * math.log(prev)/prev))
    print("--------------------------------")
    print("pi2(N)        =  " + str(count2))
    print("2CN/log(N)^2  =  " + str(2* C * prev /math.log(prev)**2))
    print("ratio         =  " + str(count2/(2* C * prev /math.log(prev)**2)))
#except:
#    print("Error reading file")