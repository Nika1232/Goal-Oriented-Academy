from turtle import *
import turtle

bob = turtle.Turtle()
speed(100)
width(5)
color("black")
shape("arrow")

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(42)
left(90)
color("gray")
begin_fill()
forward(40)
right(90)
forward(20)
right(90)
forward(40)
left(90)
end_fill()
color("black")
goto(0,0)
left(90)
forward(100)
right(45)
color("brown")
begin_fill()
forward(70)
right(90)
forward(70)
end_fill()
penup()
goto (0,0)
pendown()
left(45)
penup()
goto (20,50)
pendown()
color("black")
begin_fill()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()
penup()
goto (0,0)
pendown()
left(45)
penup()
goto (60,70)
left(45)
pendown()
forward(20)
begin_fill()
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()
penup()
goto(0,0)
pendown()

turtle = Turtle()
screen = Screen()
screen.onscreenclick(turtle.goto)
turtle.getscreen()._root.mainloop()
#draw field with mouse :D
#exitonX() :d