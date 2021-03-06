# Elijah Taylor-Kuni
# etaylork@ucsc.edu
# Programming Assignment 3
# A guessing game that takes a random number and for the user to have three tries to guess that number.
# Program informs the user if he or she is too high or too low and if they don't get it on their
# third try they lose the game. 

import random 

def guessOutput(x, rand):
   if(x < rand):
     return ("Your guess is too low.\n")
   elif(x > rand):
        return ("Your guess is too high.\n ")
   elif(x == rand):
     return ("You win!\n")
#end of GuessOutput

print("\nI'm thinking of an integer in the range of 1 to 10. You have three guesses.\n ")
ranNum =  random.randint(1,10)# uses random func to get a random int 

guessOne = int(input("Enter your first guess: "))
print(guessOutput(guessOne,ranNum))
if(guessOne == ranNum): exit()

guessTwo = int(input("Enter your second guess: "))
print(guessOutput(guessTwo,ranNum))
if(guessTwo == ranNum): exit()

guessThree = int(input("Enter your third guess: "))
print(guessOutput(guessThree,ranNum))
if(guessThree == ranNum): exit()

print("you lose. the number was "+ str(ranNum) +".\n")
