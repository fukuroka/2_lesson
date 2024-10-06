class Toy:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Название: {self.name}; Цвет: {self.color}'

class AnimalToy(Toy):
    def __init__(self,name,color):
        super().__init__(name,color)
        self.toy_type = 'Животное'

class CartoonToy(Toy):
    def __init__(self,name,color):
        super().__init__(name,color)
        self.toy_type = 'Персонаж мультфильма'

class ToyFactory:

    def create_toy(self,name,color,toy_type):
        print('Закупается сырье для игрушки')
        self.purchase_materials(name)

        print('Начинается пошив игрушки')
        self.sew(name)

        print('Начинается покраска игрушки')
        self.paint(name)

        print('Игрушка готова!\n')
        if toy_type == 'Животное':
            return AnimalToy(name,color)
        elif toy_type == 'Персонаж мультфильма':
            return CartoonToy(name,color)
        else:
            print('Неверный тип игрушки!')

    def purchase_materials(self,name):
        print(f'Материалы для игрушки {name} закуплены!')

    def sew(self,name):
        print(f'Игрушка {name} сшита!')

    def paint(self,name):
        print(f'Игрушка {name} покрашена!')

factory = ToyFactory()
new_animal_toy = factory.create_toy('Медвежонок', 'Коричневый', 'Животное')
new_cartoon_toy = factory.create_toy('Карлсон','Белый','Персонаж мультфильмаааа')

