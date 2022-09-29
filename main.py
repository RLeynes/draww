import turtle
import random

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies by @iNode.code") 
wn.bgcolor("black") 
wn.setup(width=800, height=600) 
wn.tracer(0)


player = turtle.Turtle()
player.speed(0) 
player.shape("turtle") 
player.color("white") 
player.penup() 
player.goto(0, -250) 
player.direction = "stop" 

good_guys = []

for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0) 
    good_guy.shape("square") 
    good_guy.color("blue") 
    good_guy.penup() 
    good_guy.goto(-100, 250) 
    good_guy.speed = random.randint(1, 2) 
    good_guys.append(good_guy) 

bad_guys = []

for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0) 
    bad_guy.shape("triangle") 
    bad_guy.color("red") 
    bad_guy.penup() 
    bad_guy.goto(100, 250) 
    bad_guy.speed = random.randint(1, 2) 
    bad_guys.append(bad_guy) 

pen = turtle.Turtle() 
pen.hideturtle() 
pen.speed(0) 
pen.shape("turtle") 
pen.color("white")
pen.penup() 
pen.goto(0, 260) 
font = ("Courier", 24, "normal") 
pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) 

def go_left():
    player.direction = "left"
    player.shape("turtle") 

def go_right():
    player.direction = "right"
    player.shape("turtle") 
    

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()

    if player.direction == "left": 
        x = player.xcor() 
        x -= 1 
        player.setx(x) 
    
    if player.direction == "right": 
        x = player.xcor() 
        x += 1 
        player.setx(x)    

    for good_guy in good_guys: 
        y = good_guy.ycor() 
        y -= good_guy.speed 
        good_guy.sety(y) 


        if y < -300:
            x = random.randint(-380, 380) 
            y = random.randint(300, 400) 
            good_guy.goto(x, y) 

        if good_guy.distance(player) < 40: 
            x = random.randint(-380, 380) 
            y = random.randint(300, 400) 
            good_guy.goto(x, y) 
            score += 10 
            pen.clear() 
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font) 

    for bad_guy in bad_guys: 
        y = bad_guy.ycor() 
        y -= bad_guy.speed 
        bad_guy.sety(y) 

        if y < -300:
            x = random.randint(-380, 380) 
            y = random.randint(300, 400) 
            bad_guy.goto(x, y) 

        if bad_guy.distance(player) < 40: 
            x = random.randint(-380, 380) 
            y = random.randint(300, 400) 
            bad_guy.goto(x, y) 
            score -= 10 
            lives -= 1 
            pen.clear() 
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=font)
       
wn.mainloop()