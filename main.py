import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False


    if player.ycor() == player.finish_line_y:
        player.reset_player()
        car_manager.increase_speed()
        scoreboard.update_scoreboard()

screen.exitonclick()