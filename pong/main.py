import turtle
import sys
from Objects import Paddle, Screen, Ball, Score
import os
import math

def bounceSound():
    os.system("aplay bounce.wav&")

widthScreen = 800
heightScreen = 600
wm = Screen("Pong", widthScreen, heightScreen)

marginPaddle = 50
# LEFT PADDLE
paddle_a = Paddle("left", widthScreen, heightScreen, marginPaddle)

# RIGHT PADDLE
paddle_b = Paddle("right", widthScreen, heightScreen, marginPaddle)

#BALL
ball = Ball(0.1)


# PEN
topSide = (heightScreen / 2) - marginPaddle
pen = Score(0, topSide)
pen.hideturtle()

score_a = 0
score_b = 0
pen.update(score_a, score_b)


wm.listen()
wm.onkeypress(lambda: paddle_a.up(), "w")
wm.onkeypress(lambda: paddle_a.down(), "s")
wm.onkeypress(lambda: paddle_b.up(), "Up")
wm.onkeypress(lambda: paddle_b.down(), "Down")

# Main loop
while True:
    wm.update()

    # MOVE THE Ball
    ball.move()

    # BORDER CHANGING
    ballTopLimit = (heightScreen / 2 ) - ball.height
    ballBottomLimit = (heightScreen / -2) + ball.height

    if ball.ycor() > ballTopLimit:
        ball.sety(ballTopLimit)
        ball.dy = -0.1
    elif ball.ycor() < ballBottomLimit:
        ball.sety(ballBottomLimit)
        ball.dy = 0.1

    ballRightLimit = (widthScreen / 2) - ball.width
    ballLeftLimit = (widthScreen / -2) + ball.width

    # SCORING
    if ball.xcor() < ballLeftLimit or ball.xcor() > ballRightLimit:
        score_a = score_a + 1 if ball.xcor() > 0 else score_a
        score_b = score_b + 1 if ball.xcor() < 0 else score_b
        ball.goto(0,0)
        ball.dx *= -1
        bounceSound()
        pen.update(score_a,score_b)


    # BALL AND BORDER COLISSION
    sameXcordPaddleB = abs(paddle_b.xcor() - ball.xcor()) < 0.01
    sameYcordPaddleB = abs(ball.ycor() - paddle_b.ycor()) < paddle_b.height
    paddle_bHitBall = sameXcordPaddleB and sameYcordPaddleB
    if paddle_bHitBall:
        print(paddle_bHitBall)
        ball.setx(paddle_b.xcor() - paddle_b.width)
        ball.dx *= -1
        bounceSound()

    sameXcordPaddleA = abs(paddle_a.xcor()- ball.xcor()) < 0.01
    sameYcordPaddleA = abs(ball.ycor() - paddle_a.ycor()) < paddle_a.height
    paddle_aHitBall = sameXcordPaddleA and sameYcordPaddleA
    if paddle_aHitBall:
        ball.setx(paddle_a.xcor() + paddle_a.width)
        ball.dx *= -1
        bounceSound()
