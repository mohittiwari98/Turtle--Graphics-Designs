#used turtle model
#import turtle
from turtle import *
#change colors if you want
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'white']
speed(0)
bgcolor('black')
for x in range(200):
    pencolor(colors[x % 6])
    width(2)
    forward(x*1.2)
    left(59)
