def isop(string):
    if string in "+-*/":
        return True
    return False

string = input()
strings = string.split()
backtable = [-1]* len(strings)



#the idea is to search for pairs of numbers followed by an operation until we have a list of length 1
while (len(strings)>1):
    #search for a pair of numbers followed by an operator
    pos = 0
    while (pos < len(strings)):
        if (isop(strings[pos])== False) and (isop(strings[pos+1]) == False) and (isop(strings[pos+2]) == True):
            #found a match, reduce it
            #first we see if the operator is stronger than the right ops
            if strings[pos+2] in "*/":
                if backtable[pos] >0:
                    strings[pos] = "(" + strings[pos] + ")"
                if backtable[pos+1] > 0:
                    strings[pos+1] = "(" + strings[pos+1] + ")"
                elif strings[pos+2] == "/" and backtable[pos+1] == 0:
                    strings[pos+1] = "( " +  strings[pos+1]+ ")"

                backtable[pos] = 0
            else:
                if strings[pos+2] == "-":
                    if backtable[pos+1] == 1:
                        strings[pos+1] = "(" + strings[pos+1] + ")"
                    backtable[pos] = 2
                else:
                    backtable[pos] = 1
                    
            strings[pos] = strings[pos] + " " + strings[pos+2] + " " + strings[pos+1]

            #shrink everything to the left
            pos += 1
            while ( pos < len(strings)-2):
                strings[pos] = strings[pos+2]
                backtable[pos] = backtable[pos+2]
                pos +=1
            
            strings = strings[:-2]

            #break, begin again from the beginning
            break
        pos+=1

print(strings[0])