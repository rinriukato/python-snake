from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

START_SIZE = 3
GAME_SPEED = 0.05
COLLISION_DIST_IN_PX = 17

# Initialize screen and snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Listen for key inputs to control snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()
    # Check if snake is colliding with tail
    if snake.check_tail_collision():
        scoreboard.end_game_text()
        game_is_on = False

    # Check collisions with screen
    if snake.check_out_of_bounds():
        # snake.destroy_self()
        scoreboard.end_game_text()
        game_is_on = False

    # Do collision with food
    if snake.head.distance(food) < COLLISION_DIST_IN_PX:
        food.set_new_location()
        snake.grow()
        scoreboard.increment_score()

screen.exitonclick()
