#Elijah Taylor-Kuni
#etaylork@ucsc.edu
#1371815
#Assignment 5
#Program is like a guessing game where the computer tries to guess your number from a range of low to high
#uses the binary search algorithm to find your number 

# ask for user input 
print("Enter two numbers, low then high.")
L = []
low = int(input("low = "))
high = int(input("high = "))
print()

while low > high:
   print("Please enter the smaller followed by the larger number. ")
   low = int(input("low = "))
   high = int(input("high = "))
   print()

print("Think of a number in the range of "+str(low)+" to "+str(high)+".\n")

#make a list of numbers to use for the guesses 
for i in range(low,high+1):
   L.append(i)

#implement binarysearch on the list to find the correct number
left = low 
right = high 
count = 0 

while left <= right:
   m = (left+right)//2

   # case where the left side and right side meet 
   if left == right:
     print("Your number is "+ str(m)+". I found it in " + str(count) +" guesses.")
     break 
     
   # gets user input on for less than, greater than, or equal to
   print("Is your number Less than, Greater than, or Equal to " + str(m))
   answer = input("Type 'L', 'G' or 'E': ")
   print()
   while  answer not in ('L' , 'l','E','e','G','g'):
      answer = input("please type 'L', 'G' or 'E': ")
      print()
      

   # implementing the binary search alogrithm
   if answer == 'E' or answer == 'e':
      count += 1
      if count == 1: 
         print("I found your number in 1 guess.")
      else:
         print("Your number is "+ str(m)+". I found it in " + str(count) +" guesses.")
      break
   elif answer == 'L' or answer == 'l':
      right = m - 1
      count += 1
   elif answer == 'G' or answer == 'g':
      left = m + 1
      count += 1
   
   # Case where the answers have not been consistent 
   if left > right:
      print("Your answers have not been consistent.")
   
      
print()    
