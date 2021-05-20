from turtle import Turtle
# FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=("Courier", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Courier", 24, "bold"))




