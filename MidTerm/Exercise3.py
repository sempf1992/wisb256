N = int(input()) + 1
ls = [0] * (N)
ls[3] = 1
pos = 4
while ( pos < N):
    ls[pos] = ls[pos-1] + ls[pos-2] + ls[pos-3] + ls[pos-4]
    pos+=1
print(str(ls[N-1]))