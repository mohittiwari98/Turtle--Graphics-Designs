#import turtle
from turtle import *

speed(10)
#change color according to you
color('green')
bgcolor('black')
b = 200

while b > 0:
   left(b)
   forward(b*3)
   b = b-1
