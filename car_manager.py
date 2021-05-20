from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5
        self.move_increment = 5

    def create_car(self):
        car_creation_chance = random.randint(1, 6)
        if car_creation_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 300)
            new_car.goto(300, random_y)

            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.back(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += self.move_increment

