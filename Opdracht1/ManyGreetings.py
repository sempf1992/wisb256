# This is the first hand in exercise.

Name = input('Name? ')
try:
   Amount = int(input("How many greetings? "))
   print( str(Amount)+ " x Hello, " + Name + "!")
except Exception, e:
   print("Error, "+Amount+ " is not a number")