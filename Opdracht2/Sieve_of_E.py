#import important information
import sys
import time

#set begin time
T1 = time.clock()

#read commandline
#try:
if True:
    N = int(sys.argv[1])
    outfile = sys.argv[2]
    primes = []
    ls = (N+1) * [True]
    ls[0] = False
    ls[1] = False
    count = 0
    with open(outfile, 'r+') as f:
        #update everything to primes
        i = 2
        while ( i <= N):
        
            #if current number is a prime
            if ls[i] == True:
            
                #add i to primes
                primes.append(i)
                f.write(str(i)+ "\n")
            
                count +=1
                #remove all multiples
                j = 2*i
            
                while ( j <= N):
                    ls[j] = False
                    j += i
            i += 1

#except:
#    print("Some input has been wrong")

#set end time
T2 = time.clock()
print ("Found " +  str(count) + " Prime numbers smaller than "+ str(N)+ " in " + str( T2- T1) + "sec.")