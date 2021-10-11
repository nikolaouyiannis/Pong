from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create screen
screen = Screen()
# Set screen dimensions
screen.setup(width=800, height=600)
# Set screen color
screen.bgcolor("black")
screen.title("Pong")
# Turn off animation with tracer
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # print(f"Paddle: {r_paddle.xcor()}, {r_paddle.ycor()}")
    time.sleep(ball.move_speed)
    screen.update()
    # print(f"While/ Before Move: {ball.xcor()}, {ball.ycor()}")
    ball.move()
    # print(f"Before if/ Before bounce: {ball.xcor()}, {ball.ycor()}")

    # Top wall collision
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce_y()
        # print(f"After if/ After bounce: {ball.xcor()}, {ball.ycor()}")
    
    # Paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -400 :
        ball.reset_position()
        scoreboard.r_point()      


    


screen.exitonclick()

