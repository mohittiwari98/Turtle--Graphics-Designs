# importing Required modules
#import turtle
#import
import turtle
import colorsys

# Create window to Display Pattern
t = turtle.Turtle()
s = turtle.Screen()

# Setting Background color
s.bgcolor("black")

# Speed of turtle to draw pattern
t.speed(0)

n = 36
h = 0

# Loop for drawing Pattern
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150
