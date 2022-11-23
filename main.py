import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Turtle")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="w")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    if random.randint(1, 5) == 1:
        car_manager.create_car()

    for car in car_manager.cars_list:
        if (car.distance(player)) < 25 and (player.ycor() - car.ycor() <= 12):
            print(car.ycor())
            print(player.ycor())
            game_is_on = False

    if player.ycor() > 280:
        player.refresh()
        car_manager.level_up()
        scoreboard.update_scoreboard()

    for car in car_manager.cars_list:
        if car.xcor() < -320:
            car.hideturtle()
            car_manager.cars_list.remove(car)

    car_manager.move_all()
