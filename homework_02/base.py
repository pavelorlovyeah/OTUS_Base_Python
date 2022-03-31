from exceptions import LowFuelError, NotEnoughFuel

class Vehicle:
    # weight [kg], fuel [liters], fuel_consumption [liters/100 km]

    def __init__(self, weight = 0, started = False, fuel = 0, fuel_consumption = 0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                return self.started
            else:
                raise LowFuelError
        return self.started

    def move(self, dist):
        range = self.fuel / self.fuel_consumption * 100
        print('distance', dist, 'km')
        print('range', range, 'km')
        if dist <= range:
            #print('remaining fuel:', fuel = (range - dist) * self.fuel_consumption / 100, 'l')
            self.fuel = (range - dist) * self.fuel_consumption / 100
            return self.fuel
        else:
            raise NotEnoughFuel


audi = Vehicle(1000, True, 10, 10)
print(vars(audi))
print(audi.start())
print(audi.started)
print(audi.move(15))