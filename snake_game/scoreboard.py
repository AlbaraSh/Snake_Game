from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',24,'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.goto(x = 0, y = 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   Highscore: {self.highscore}', align = ALIGNMENT, font = FONT)

    def add_Score(self):
        self.score += 1
        self.update_scoreboard()  

    def reset(self):
        if self.score > self.highscore: 
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()