# Elijah Taylor-Kuni 
# etaylork@ucsc.edu
# programming assignment 2
# a python program that uses the turtle library to create a n-side star. takes user
# input and creates a picture of a star with the given sides that the user inputs. 

import turtle

s = int(input("Enter a odd integer greater than or equal to 3: ")) #user input to get sides

wm = turtle.Screen() #creates the screen

#components of the star
star = turtle.Turtle()
star.pensize(2)
star.color("blue","lime") #creates pen color and fill color 
wm.title(str(s)+"-star")
star.hideturtle()
star.speed("fastest")

# creating the star
star.penup()
star.goto(-150,0)
star.pendown()
star.begin_fill()

# loop in order to make the star
for i in range(s):
   star.forward(300)
   n = 180 - 180/s
   star.right(n)
   star.dot(10,"red") #creates the end point of the star
star.end_fill()

wm.mainloop()
