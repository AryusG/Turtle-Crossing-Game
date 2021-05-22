from turtle import Turtle
# FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.high_score = 1
        self.hideturtle()
        self.penup()
        self.goto(-160, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.level >= self.high_score:
            self.high_score = self.level
        self.clear()
        self.write(f"Level: {self.level} Highscore: {self.high_score}", align='center', font=("Courier", 14, "bold"))

    def reset_scoreboard(self):
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1





