from turtle import Screen, Turtle
SNAKE_SIZE = 20
SNAKE_START_LEN = 3
MOVE_DIST = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SCREEN_BOUNDS = 300
TAIL_COLLISION_DIST = 10


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for x in range(SNAKE_START_LEN):
            t1 = Turtle(shape='square')
            t1.color('white')
            t1.penup()
            t1.setpos(x=(x * -SNAKE_SIZE), y=0)
            self.snake_body.append(t1)

    def move(self):
        start = len(self.snake_body) - 1
        for seg_num in range(start, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        # Move the head
        self.head.forward(MOVE_DIST)

    def up(self):
        # Prevent player from moving into itself
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Prevent player from moving into itself
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Prevent player from moving into itself
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Prevent player from moving into itself
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        t1 = Turtle(shape='square')
        t1.color('white')
        t1.penup()
        new_x = self.snake_body[-1].xcor()
        new_y = self.snake_body[-1].ycor()
        t1.setpos(new_x, new_y)
        self.snake_body.append(t1)

    def check_out_of_bounds(self) -> bool:
        cur_x = self.head.xcor()
        cur_y = self.head.ycor()

        return ((cur_x > SCREEN_BOUNDS or cur_x < -SCREEN_BOUNDS)
                or (cur_y > SCREEN_BOUNDS + 10 or cur_y < -SCREEN_BOUNDS - 10))

    def check_tail_collision(self) -> bool:
        # Check everything besides the head
        for seg in self.snake_body[1:]:
            if self.head.distance(seg) < TAIL_COLLISION_DIST:
                return True

        return False

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

