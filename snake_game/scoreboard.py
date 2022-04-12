from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
GAME_OVER_FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.scorestr = "Score = " + str(self.score)
        self.penup()
        self.pencolor("white")
        self.setposition(0,280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=GAME_OVER_FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


