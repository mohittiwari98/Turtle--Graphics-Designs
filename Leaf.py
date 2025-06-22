#import turtle model
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('lightgreen')
t.speed(0)

for i in range(120):
    t.circle(190-i,90)
    t.left(90)
    t.circle(190-i,90)
    t.left(18)

turtle.done()   
