# Задание 1. Светофор. Сделал без усложнения с проверкой.

from termcolor import colored
from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = 'Красный'

    def running(self):
        colors = [['red', 7, 'Красный'], ['yellow', 2, 'Желтый'], ['green', 7, 'Зеленый']]
        color = cycle(colors)
        while True:
            cur_color = next(color)
            self.__color = cur_color[2]
            print(colored('\r' + self.__color, cur_color[0]), end='')
            sleep(cur_color[1])


traffic_light = TrafficLight()
traffic_light.running()
