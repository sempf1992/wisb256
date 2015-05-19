string = input()
if string == "Ug!":
    print("1")
elif len(string.split())>1:
    print(str(len(string.split())))
else:
    ugs = int(string)
    if ( ugs == 1):
        output = "Ug!"
    elif (ugs == 2):
        output = "Ug ug!"
    else:
        output = "Ug " + "ug "* (ugs -2) + "ug!"
    print(output)