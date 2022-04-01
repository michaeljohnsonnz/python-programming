from turtle import * 
from random import randint 

colormode(255)

t = Turtle()

t.screen.bgcolor("black")
t.pensize(1)
t.speed(0)

def change_pen_color():
    r = randint(0,255) 
    g = randint(0,255)  
    b = randint(0,255) 
    t.color(r,g,b) 

def draw_circle(radius):
    for i in range(33):
        change_pen_color()
        t.circle(radius)
        radius = radius + 33

def draw_design():
    for i in range(33):
        draw_circle(33)
        t.right(33)

for i in range(33):
    draw_design()

done()
