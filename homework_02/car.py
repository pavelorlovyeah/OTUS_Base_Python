"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle
from engine import Engine

class Car(Vehicle):

    def __init__(self, weight = 0, started = False, fuel = 0, fuel_consumption = 0, engine = 0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine
        return self.engine



engine_1 = Engine(1.6, 4)
#print(engine_1)
bmw = Car(1200,False,65,150,0)
bmw.set_engine(engine_1)
print(bmw.engine)
print(vars(bmw))


