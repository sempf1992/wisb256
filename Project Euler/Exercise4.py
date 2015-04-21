i = 100
largest = 0
while ( i < 1000):
    j = i
    while (j < 1000):
        if i * j == int(str(i * j)[::-1]):
            if (i * j > largest):
                largest = i * j
        j +=1
    i +=1

print largest