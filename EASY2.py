class Car:
    def __init__(self,color,name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

class TownCar(Car):
    def __init__(self,color,name):
        super().__init__(color,name)
        self.speed = 150


class SportCar(Car):
    def __init__(self,color,name):
        super().__init__(color,name)
        self.speed = 250


class WorkCar(Car):
    def __init__(self,color,name):
        super().__init__(color,name)
        self.speed = 120


class PoliceCar(Car):
    def __init__(self,color,name):
        super().__init__(color,name)
        self.speed = 150
        self.is_police = True

    def arrest(self,car):
        print(f'Полицейская машина {self.name} задержала машину {car.name}')

car_t = TownCar('silver','Toyota')
car_s = SportCar('red','Porsche')
car_w = WorkCar('orange','Kamaz')
car_p = PoliceCar('blue', 'Ford')
car_t.go()
car_s.stop()
car_w.turn('направо')
car_p.arrest(car_t)
print(car_p.speed)