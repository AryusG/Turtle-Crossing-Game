from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.hideturtle()
        self.penup()
        self.goto(-160, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} Highscore: {self.high_score}", align='center', font=("Courier", 14, "bold"))

    def reset_scoreboard(self):
        if self.level >= self.high_score:
            self.high_score = self.level
            with open("data.txt", "w") as data:
                data.write(f"{self.level}")
        self.level = 1
        self.update_scoreboard()


    def increase_level(self):
        self.level += 1





