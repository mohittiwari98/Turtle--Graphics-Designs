#import turtle libary
from turtle import*
#change colour if you required
bgcolor('black')
color('yellow')
speed(11)
right(45)
#using for loop
for i in range(150) :
    circle(30)
    #using conditional
    if 7 < i < 62 :
        left(5)
    if 80 < i < 133 :
        right(5)
    if i < 80 :
        forward(10)
    else :
        forward(5)
