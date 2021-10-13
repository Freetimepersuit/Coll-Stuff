# Rock, Paper, Scissors Game

import turtle
import time
import random

score = 0
high_score = 0

# Setup
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Test")
wn.setup(width= 600, height = 600)
wn.tracer(0)



# Snake
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.goto(0, 0)
head.speed(0)
head.penup()
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 100)
food.speed(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 High Score: 0", align="center", font=("Arial", 34, "normal"))


segments = []


# Input
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


# Move
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Mainloop
while True:
    wn.update()

    # Border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Gide Segments
        for segment in segments:
            segment.goto(5000, 5000)

        # Clear Segment list
        segments.clear()

        # Reset score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score{}".format(score, high_score), align="center", font=("Arial", 34, "normal"))
    # Collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 260)
        food.goto(x, y)

        # Add Segemtns
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("red")
        new_segments.penup()
        segments.append(new_segments)

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score{}".format(score, high_score), align="center", font=("Arial", 34, "normal"))
    
    # Move the last segments first in revsere order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    # Move segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    # Check for Bodycolission
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide Segments
            for segment in segments:
                segment.goto(5000, 5000)

            # Clear Segment list
            segments.clear()
        
            # Reset score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score{}".format(score, high_score), align="center", font=("Arial", 34, "normal"))   

    time.sleep(0.1)



wn.mainloop()