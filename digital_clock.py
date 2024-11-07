'''
Digital Clock with  Python Turtle Graphics
Code By - Ahsun Ahmed Sun
'''

# Importing libraries
import time  
import datetime as dte  
import turtle
    
# Creating Two Turtles - One for Rectangle & Another for Time
tt1 = turtle.Turtle()  
tt2 = turtle.Turtle()


# Creating Screen
screen = turtle.Screen()  
screen.bgcolor("green")


# Fetching Current Timings
hour = dte.datetime.now().hour
second = dte.datetime.now().second
minute = dte.datetime.now().minute


# Setting Pensize and Color
tt2.pensize(3)  
tt2.color('white')
tt2.hideturtle()

# Adjusting Location
tt1.penup()
tt1.forward(-120)
tt1.pendown()

tt2.penup()
tt2.forward(-120)
tt2.pendown()


# Creating Rectangle for Clock
for j in range(2):  
    tt2.forward(200)  
    tt2.left(90)  
    tt2.forward(70)  
    tt2.left(90)
    

# Displaying Time
while True:
    tt1.hideturtle()
    tt1.clear()
    # Displaying the generated time  
    tt1.write(str(hour).zfill(2) + ":"+str(minute).zfill(2)+":"+ str(second).zfill(2),font=("Callibri Narrow", 37, "bold"))

    time.sleep(1)  
    second += 1  
    if second == 60:  
       second = 0  
       minute += 1  
    if minute == 60:  
       minute = 0  
       hour += 1  
    if hour == 13:  
       hour = 1
    tt1.clear()
