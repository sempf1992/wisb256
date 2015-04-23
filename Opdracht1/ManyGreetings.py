# This is the first hand in exercise.

Name = input('What is your name? ')
try:
   Amount = int(input("How many greetings? "))
   print( str(Amount)+ " x Hello, " + Name + "!")
except:
   print("Error, "+Amount+ " is not a number")