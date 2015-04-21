# This is the first hand in exercise.

Name = raw_input('Name? ')
try:
    Amount = int(raw_input("How many times? "))
    print( str(Amount)+ " x Hello, " + Name + "!")
except Exception, e:
    print("Error, "+Amount+ " is not a number")