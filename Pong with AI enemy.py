# Pong

import turtle
import winsound

# Setup
wn = turtle.Screen()
wn.title("Cool Pong game")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len = 1)
paddle_right.color("red")
paddle_right.penup()
paddle_right.goto(350, 0)



# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5,stretch_len= 1)
paddle_left.color("red")
paddle_left.penup()
paddle_left.goto(-350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Score

pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0   Player B: 0", align="center", font=("Arial", 24, "normal"))


# Movement Right Paddle
def paddle_right_up():
    y = paddle_right.ycor()
    paddle_right.sety(y + 20)
def paddle_right_down():
    y = paddle_right.ycor()
    paddle_right.sety(y - 20)

# Movement Left Paddle
def paddle_left_up():
    y = paddle_left.ycor()
    paddle_left.sety(y + 20)
def paddle_left_down():
    y = paddle_left.ycor()
    paddle_left.sety(y - 20)


# Keybinds
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

#Main loop
while True:
    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borde Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball colliosion
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor()+ 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor()+ 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # Ai Player
    if paddle_right.ycor() < ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 15:
        paddle_right_up()
    
    elif paddle_right.ycor() > ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 15:
        paddle_right_down()

