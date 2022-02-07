import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

level = Scoreboard()
level.start()

car_manager = CarManager()


screen.listen()
screen.onkeypress(player.moveUp , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.createCar()
    car_manager.moveCars()

    if player.hasWon():
        level.levelUp()
        car_manager.increaseSpeed()
        time.sleep(0.01)
   
    elif player.hasLost(car_manager.cars):
        level.reset()
        
    

    screen.update()
    