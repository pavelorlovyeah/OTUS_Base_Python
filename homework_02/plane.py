"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle

class Plane(Vehicle):

    def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0,
                 cargo = 0,
                 max_cargo = 0
                 ):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, extra_cargo):
        final_cargo = self.cargo + extra_cargo
        if final_cargo < self.max_cargo:
            self.cargo = final_cargo
            return self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_init = self.cargo
        self.cargo = 0

# airbus = Plane(0,0,0,0,500,1000)
# print(airbus.max_cargo)
# airbus.load_cargo(250)
# print(airbus.cargo)
# airbus.remove_all_cargo()
# print(airbus.cargo)
# print(vars(airbus))



