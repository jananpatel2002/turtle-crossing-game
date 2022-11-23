import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_AMOUNT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 280))
        car.setheading(180)
        self.cars_list.append(car)

    def move_all(self):
        for car in self.cars_list:
            car.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
