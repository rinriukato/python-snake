from turtle import Turtle

FONT = "Arial"
FONT_SIZE = 15
FONT_TYPE = 'normal'
START_X_COORD = 0
START_Y_COORD = 270
FILE_NAME = "high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(START_X_COORD, START_Y_COORD)
        self.update_text()

    def increment_score(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(arg=f"Score : {self.score} | High Score : {self.high_score}", move=False, align='center',
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def end_game_text(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align='center',
                   font=(FONT, FONT_SIZE, FONT_TYPE))

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
        self.write_high_score()
        self.score = 0
        self.update_text()

    def get_high_score(self) -> int:
        return self.high_score

    def read_high_score(self) -> int:
        with open(FILE_NAME, mode='r') as file:
            file_high_score = file.read()
            print("reading high score from file")
            return int(file_high_score)

    def write_high_score(self):
        with open(FILE_NAME, mode='w') as file:
            high_score = self.high_score
            file.write(str(high_score))
