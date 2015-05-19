lines = int(input())
count = 0;
line = 0;
while (line < lines):
    for letter in input():
        if letter == "#":
            count+=1
    line+=1
print("Om de hekjes in dit weiland te verven heb je "+ str(5 * count) + " liter verf nodig")