import turtle

ts=turtle.getscreen()
t=turtle.Turtle()

t.begin_fill()
t.color("skyblue")
#head
t.left(90)
t.forward(300)
#right body
t.right(90)
t.forward(300)
#lower body
t.right(90)
t.forward(300)
#left body
t.right(90)
t.forward(300)
t.end_fill()

#inner box

t.color("white")
t.penup()
t.right(90)
t.forward(250)
t.right(90)
t.forward(30)
t.pendown()

#colored inner box
t.begin_fill()
t.forward(240)
t.right(90)
t.forward(90)
t.right(90)
t.forward(240)
t.right(90)
t.forward(90)
t.end_fill()

#eyes
t.color("black")

#left_eye
t.penup()
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

#right_eye
t.penup()
t.left(90)
t.forward(50)

