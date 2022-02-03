from turtle import Screen
from middle import Middle
from paddle import Paddle
from ball import Ball
from scoreboard import Scorebord
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


for i in range(305, -305, -40):
    mid = Middle()
    mid.createMiddle(i)

paddle_left = Paddle()
paddle_left.createPaddle((-380, 0))

paddle_right = Paddle()
paddle_right.createPaddle((372, 0))

screen.listen()
screen.onkeypress(paddle_left.moveUp, "w")
screen.onkeypress(paddle_left.moveDown, "s")
screen.onkeypress(paddle_right.moveUp, "Up")
screen.onkeypress(paddle_right.moveDown, "Down")

ball = Ball()
ball.createBall()

sb = Scorebord()
sb.display()

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Collision with the wall:
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
        
    # Collision with the right paddle:
    # if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
    #     ball.hit()

    # Collision with the left paddle:
    # if ball.distance(paddle_left) < 50 and ball.xcor() < -340:
    #     ball.hit()

    #  Collision with the paddle:
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 340) or (ball.distance(paddle_left) < 50 and ball.xcor() < -340):
        ball.hit()
    
    # If ball is out of bounds:
    # if (ball.xcor() > 380) or ( ball.xcor() < -380):
    #     time.sleep(1)
    #     ball.reset()
    
    #  If right paddle misses:
    if ball.xcor()>380:
        sb.l_score += 1
        sb.display()
        time.sleep(1)
        ball.reset()

    #  If left paddle misses:
    if ball.xcor()<-380:
        sb.r_score += 1
        sb.display()
        time.sleep(1)
        ball.reset()
        


screen.exitonclick()

