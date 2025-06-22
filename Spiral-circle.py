#import turtle
from turtle import *

bgcolor('black')
speed(0)

for i in range(180):
   color('red')
   circle(i)
   color('yellow')
   circle(i*0.7)
   right(9)
   forward(2)

done()   
