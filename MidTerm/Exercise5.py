string = input()
strings = string.split()
#our program works by simplyfing the equation step by step
pos1 = 0 #current leftmost number
pos2 = 0 #current position we are evualating

Op1 = 0# operand1
Op2 = 0# operand2

#create a list of operations
ops = "+-*/"

#first transform the strings to floats
pos = 0
while (pos < len(strings)):
    try:
        strings[pos] = float(strings[pos])
    except:
        strings[pos] = strings[pos]
    pos +=1

#the idea is to search for pairs of numbers followed by an operation until we have a list of length 1
while (len(strings)>1):
    #search for a pair of numbers followed by an operator
    pos = 0
    while (pos < len(strings)):
        
        bool1 = (type(strings[pos])   == type(1.0))
        bool2 = (type(strings[pos+1]) == type(1.0))
        bool3 = (type(strings[pos+2]) != type(1.0))
        
        if bool1 and bool2 and bool3:
        #found a match, reduce it
            if strings[pos+2] == "+":
                strings[pos] = strings[pos] + strings[pos+1]
            if strings[pos+2] == "-":
                strings[pos] = strings[pos] - strings[pos+1]
            if strings[pos+2] == "*":
                strings[pos] = strings[pos] * strings[pos+1]
            if strings[pos+2] == "/":
                strings[pos] = strings[pos] / strings[pos+1]
            
            #shrink everything to the left
            pos += 1
            while ( pos < len(strings)-2):
                strings[pos] = strings[pos+2]
                pos +=1
            
            strings = strings[:-2]

            #break, begin again from the beginning
            break
        pos+=1

print("{0:.3f}".format(strings[0]))