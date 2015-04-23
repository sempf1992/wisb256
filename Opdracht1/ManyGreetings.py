# This is the first hand in exercise.

Name = raw_input('What is your name? ')
try:
   Amount = int(raw_input("How many greetings? "))
   print( str(Amount)+ " x Hello, " + Name + "!")
except Exception, e:
   print("Error, "+Amount+ " is not a number")