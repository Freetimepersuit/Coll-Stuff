# Cookie clicker basic

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.setup(800,600)
wn.title("Cookie clicker")

wn.register_shape("C:/Users/timpu/OneDrive/Desktop/Cookie/cookie.gif")

cookie = turtle.Turtle()
cookie.shape("C:/Users/timpu/OneDrive/Desktop/Cookie/cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,400)
pen.write(f"Clicks: {clicks}", align="center", font=("Arial", 30,"normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Arial", 30,"normal"))

cookie.onclick(clicked)

wn.mainloop()