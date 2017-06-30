#-----------------------------------------------------------------------------
#Elijah Taylor-Kuni
#etaylork
#Pa7 
# A module program that inovles vector arithmetic. Made a module that computes
# differenct vector (lists) arithmatic by creating different types of functions
#-----------------------------------------------------------------------------
"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  

"""
#------------------------------------------------------------------------------
# import standard library modules
#------------------------------------------------------------------------------
import random 
import math 
#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------

def add(u, v):
	""" 
	Return the vector sum u+v.
	"""
	s = []
	for i in range(len(u)):
		s.append(u[i] + v[i])
	return s

# end add()

def negate(u):
	"""
	Return the negative -u of the vector u.
	"""
	neg = []
	for i in range(len(u)):
		neg.append(u[i] * -1)
	return neg

# end negate()   

def sub(u, v):
	""" 
	Return the Vector difference u-v.
	"""
	diff = []
	for i in range(len(u)):
		diff.append(u[i] - v[i])
	return diff

# end sub()

def scalarMult(c, u):
   """ Return the scalar product cu of the number c by the vector u. """
   result = []
   for i in range(len(u)):
    	result.append(c*u[i])
   return result 
# end scalarMult()

def zip(u, v):
   """ 
   Return the component-wise product of u with v.
   """
   result = []
   for i in range(len(u)):
   	  result.append(u[i]*v[i])
   return result 
# end zip()

def dot(u, v):
	""" 
	Return the dot product of u with v. 
	"""
	result = 0
	x = zip(u,v)
	for i in range(len(x)):
	   result += x[i]
	return result  

# end dot()

def length(u):
	""" 
	Return the (geometric) length of the vector u.
	"""
	result = 0
	for i in range(len(u)):
		result += u[i]**2
	result = result**(1/2)
	return result 

# end length()
   
def unit(v):
	""" 
	Return a unit (geometric length 1) vector in the direction of v.
    """
	result = []
	x = length(v)
	for i in range(len(v)):
		result.append(v[i]/x)
	return result 

# end unit()

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))
# end angle()

def randVector(n, a, b):
	"""
	Return a vector of dimension n whose components are random floats
	in the range [a,b).
    """
	result = []
	for i in range(n):
	  result.append(random.random() * (b-a) + a)
	return result

# end randomVector()

