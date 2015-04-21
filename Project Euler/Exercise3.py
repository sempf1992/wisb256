import math

Target = 600851475143

sq = math.sqrt(Target)
i = 2

while ( i <= sq):
    if (Target % i == 0):
        Target = Target/i
        sq = math.sqrt(Target)
    i+=1
    
print Target