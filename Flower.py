#graphics
#used model turtle
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

for i in range(290):
    t.pencolor('yellow')
    t.circle(-i+1, 200)
    t.rt(80)

turtle.done()    
