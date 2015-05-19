def isop(string):
    if string in "+-*/":
        return True
    return False

string = input()
strings = string.split()
#our program works by simplyfing the equation step by step
pos1 = 0 #current leftmost number
pos2 = 0 #current position we are evualating

Op1 = 0# operand1
Op2 = 0# operand2

#create a list of operations
ops = "+-*/"

res = ""



#the idea is to search for pairs of numbers followed by an operation until we have a list of length 1
while (len(strings)>1):
    #search for a pair of numbers followed by an operator
    pos = 0
    while (pos < len(strings)):
        if (isop(strings[pos])== False) and (isop(strings[pos+1]) == False) and (isop(strings[pos+2]) == True):
        #found a match, reduce it
            strings[pos] = "(" + strings[pos] + " " + strings[pos+2] + " " + strings[pos+1] + ")"

            #shrink everything to the left
            pos += 1
            while ( pos < len(strings)-2):
                strings[pos] = strings[pos+2]
                pos +=1
            
            strings = strings[:-2]

            #break, begin again from the beginning
            break
        pos+=1

print(strings[0])