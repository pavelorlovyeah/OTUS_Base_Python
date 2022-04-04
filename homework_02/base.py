from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):

    # weight [kg], fuel [liters], fuel_consumption [liters/100 km]
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        #self.started = False

    def start(self):
        #if started == False:
        if self.fuel > 0:
            self.started = True
            return
        raise LowFuelError
        #return started

    def move(self, dist):
        range = self.fuel / self.fuel_consumption #* 100
        print('distance', dist, 'km')
        print('range', range, 'km')
        if dist <= range:
            self.fuel = self.fuel - dist * self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel

#audi = Vehicle(1000, 10, 10)
#print((audi))
#print(audi.started)
# audi = Vehicle(1000, True, 10, 10)
# print(vars(audi))
# print(audi.start())
# print(audi.started)
# print(audi.move(15))