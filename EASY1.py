class TownCar:
    def __init__(self,color,name):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = 150

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


class SportCar:
    def __init__(self,color,name):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = 250

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


class WorkCar:
    def __init__(self,color,name):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = 120

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


class PoliceCar:
    def __init__(self,color,name):
        self.color = color
        self.name = name
        self.speed = 150
        self.is_police = True

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def arrest(self,car):
        print(f'Полицейская машина {self.name} задержала машину {car.name}')