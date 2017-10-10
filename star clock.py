import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.hideturtle()

p = math.tan(math.radians(18))
def star(tes,pjg):
    tess.penup()
    tess.goto(-pjg/2,pjg/2*p)
    tess.pendown()
    for i in range(5):
        tes.fd(pjg)
        tes.right(144)       
star(tess,150)

tess.penup()
tess.home()
tess.stamp()

for i in range(12):
    tess.fd(100)
    tess.pendown()
    tess.fd(10)
    tess.penup()
    tess.fd(20)
    tess.pendown()
    tess.stamp()
    tess.penup()
    tess.back(130)
    tess.left(30)

wn.exitonclick()
