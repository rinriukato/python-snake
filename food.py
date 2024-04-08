from turtle import Turtle
import random

SCREEN_SIZE = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.set_new_location()

    def set_new_location(self):
        random_x = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
        random_y = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
        self.goto(random_x, random_y)
