#lees input
K = int(input())
I = 0
woordenboek = []
while ( I < K):
    woordenboek.append(input())
    I+=1
N = int(input())
I = 0
swipe = ""
while ( I < N):
    swipe = input()
    #test for match
    Match = False
    
    for woord in woordenboek:
        WordMatch = True
        if swipe[0] != woord[0]:
            WordMatch = False

        if swipe[-1] != woord[-1]:
            WordMatch = False

        pos1 = 0 #positie in het woord
        pos2 = 0 #positie in de swipe input
        
        while ( pos1 < len(woord) - 1):
            #vind de letter
            while ((pos2 < len(swipe)) and ( swipe[pos2] != woord[pos1])):
                pos2+=1
            pos1 +=1
            
        #we weten dat de laatste letter niet gelijk is aan de laatste letter van de swipe input
        if pos2 == len(swipe):
            WordMatch = False

        if WordMatch:
            Match = True
            print(woord)
            break
    if Match== False:
        print("?")
    I +=1
