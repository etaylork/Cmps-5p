#Elijah Taylor-Kuni
#Etaylork@ucsc.edu
#Assignment 4
#Primes.py is a program that takes user input for the number of primes he/she wishes to see. Then uses a a
#simple function to determine what numbers are prime numbers or a composite number. After this is done we 
#put the prime numbers into a list and print out that list 

# Simple function to tell whether A number is Prime or Not 
def isPrime(m,L):
  for n in L:
     if(m % n == 0):
       return False
  return True
 #end of isPrime function 

primes = int(input("\nEnter the number of Primes to compute: " ))
PrimeList = [2]

print("\nThe first "+str(primes)+" primes are : ")

# the loop that appends the prime numbers into PrimeList
i = 3 #start off with a number greater than 2 
while(len(PrimeList) != primes):
  if(isPrime(i,PrimeList)):
    PrimeList.append(i)
  i += 1  

#prints out the List of Prime numbers 10 items per line 
counter = 0   
for p in PrimeList:
   print(p,end=" ")
   counter +=1
   if(counter == 10):
   	 print("")
   	 counter = 0
print()
