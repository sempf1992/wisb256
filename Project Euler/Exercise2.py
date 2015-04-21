i = 1
j = 1
total = 0
while (j < 4000000):
    #check if largest (current) is even
    if (j % 2 == 0):
        total += j
    #update
    temp = j
    j = j + i
    i = temp
    
print total