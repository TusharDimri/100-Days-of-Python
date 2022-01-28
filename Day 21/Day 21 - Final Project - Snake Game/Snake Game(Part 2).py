from turtle import Screen


from snake import Snake
from food import Food
from scoreboard import Scoreboard

# 1 - Screen Setup and Creating a Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""
segment1 = Turtle()
segment2 = Turtle()
segment3 = Turtle()
segment1.color("white")
segment2.color("white")
segment3.color("white")
segment1.shape("square")
segment2.shape("square")
segment3.shape("square")
segment2.setpos(-20, 0)
segment3.setpos(-40, 0)
"""
"""
starting_positions = [(0, 0), (-10, 0), (-30, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(position[0], position[1])
    segments.append(new_segment)
"""
# 2 - Animating the Snake Segments in Screen

game_is_on = True
score = 0

"""
while(game_is_on):
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    for index in range(len(segments)-1, 0, -1):
        new_x = segments[index-1].xcor()
        new_y = segments[index-1].ycor()
        segments[index].goto(new_x, new_y) 

    segments[0].forward(10)
"""

snake = Snake()
food = Food()
score_board = Scoreboard()


# 4 - Controlling the Snake with a Keypress:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.score += 1
        score_board.display()
     
    # Detect Collision with Wall:
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() <- 295:
        game_is_on = False
        score_board.gameOver()
        
    # Detect Collision with Tail:
    # If head collides with any of the segments
            #  Trigger Game Over Sequence

    for segment in snake.segments[1:]:
        if(snake.head.distance(segment) < 10):
                game_is_on = False
                score_board.gameOver()
    
    # Alternative Logic:
    # for segment in range(1, len(snake.segments)):
    #     if(snake.head.distance(snake.segments[segment]) < 10):
    #             game_is_on = False
    #             score_board.gameOver()
        
        


screen.exitonclick()