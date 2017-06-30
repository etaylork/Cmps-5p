
#Elijah Taylor-Kuni
#etaylork
#Pa6
#A program that finds the probability of a dice game. Taking user input for how many dice
#how many sides, and how many times to roll the dice. Then finds the probibility and displaying the
#result and chances to roll that number

import random

rng = random.Random(237) # Create a randonm number generator 

#Dice function for frequency 

def throwDice(d , s):
  D = []
  for i in range(d):
      D.append(rng.randrange(1, s + 1))

  return tuple(D) 


#--- main ----------------------------------------------------

dice = int(input("\nEnter the number of dice: "))

while(dice <= 0):
    print("The number of dice must be at least 1")
    dice = int(input("Please enter the number of dice: "))


print()
sides = int(input("Enter the number of sides on each die: "))

while(sides < 2):
    print("The number of sides on each die must be at least 2 ")
    sides = int(input("Please enter the number of sides on each die: "))


print()
trials = int(input("Enter the number of trials to perform: "))

while(trials <= 0):
    print("The number of trials must be at least 1")
    trials = int(input("Please enter the number of trials to perform: "))

#perform simulation, record and print frequencies 
freq = (sides*dice) + 1
frequency = freq*[0]
for i in range(trials):
   T = throwDice(dice,sides)
   x = 0
   for i in range(len(T)):
         x = x + T[i]   
   frequency[x] += 1

# end for loop

print()

#calculate relative frequencies, probabilities and errors
relativeFrequency = [0,0]
probability = [0,0]
error = [0,0]
den = sides ** dice #denominator

for i in range(2, len(frequency)):
   relativeFrequency.append(frequency[i]/trials)
   probability.append(relativeFrequency[i]*100)
   
#end for loop

f1 = " {0:<8}{1:<14}{2:<24}{3:<25}"
f2 = 71*"-"
f3 = "{0:>4}{1:>11}           {2:<24.5f}{3:>5.2f}{4:>2}"
print(f1.format("Sum","frequency","Relative Frequency","Experimental Probability"))
print(f2)
for i in range(dice, len(frequency)):
   print(f3.format(i,frequency[i],relativeFrequency[i], probability[i],'%'))
#end fors
print()
