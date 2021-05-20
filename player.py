from turtle import Turtle

# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(90)
        self.penup()
        self.shape('turtle')
        self.starting_position = (0, -280)
        self.move_distance = 10
        self.finish_line_y = 280
        self.reset_player()

    def move(self):
        self.forward(self.move_distance)

    def reset_player(self):
        self.goto(self.starting_position)
