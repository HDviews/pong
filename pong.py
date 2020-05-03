#pong made by HD
#even though I followed a youtube tutorial
#I'm gonna try to add a twist to itttt

import turtle
import os
import winsound
import random

window = turtle.Screen()
window.title("Pong by HD")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))

winning_score = turtle.Turtle()
winning_score.speed(0)
winning_score.color("white")
winning_score.penup()
winning_score.hideturtle()
winning_score.goto(0, 20)

end_msg = turtle.Turtle()
end_msg.speed(0)
end_msg.color("white")
end_msg.penup()
end_msg.hideturtle()
end_msg.goto(0, -45)

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def nothing():
    pass

#keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    window.update()

    #moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
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
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong/bop.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong/bop.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
    
    if score_a == 5:
        winning_score.write("Paddle A Wins!", align="center", font=("courier", 24, "normal"))
        ball.goto(0,0)
        end_msg.write("Thanks for Playing!", align="center", font=("courier", 24, "normal"))
        if window.onkeypress(nothing, any):
            break

    
    if score_b == 5:
        winning_score.write("Paddle B Wins!", align="center", font=("courier", 24, "normal"))
        ball.goto(0,0)
        end_msg.write("Thanks for Playing!", align="center", font=("courier", 24, "normal"))
        if window.onkeypress(nothing, any):
            break
