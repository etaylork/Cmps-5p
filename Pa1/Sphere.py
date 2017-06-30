#--------------------------------------------------------------
# Elijah Taylor-Kuni
# etaylork@ucsc.edu
# pa1
# a program that allows you to find the volume and surface area of
# a sphere with inputing the radius
#----------------------------------------------------------------
import math

radius = float(input("Enter the radius of the sphere: "))
volume = 4/3*math.pi*math.pow(radius,3)
surface_area = 4*math.pi*math.pow(radius,2)
print("The volume is:", volume) 
print ("The surface area is:", surface_area)
