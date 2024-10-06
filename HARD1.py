class Toy:
    def __init__(self,name,color,toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f'Название: {self.name}; Цвет: {self.color}; Тип игрушки: {self.toy_type}'

class ToyFactory:

    def create_toy(self,name,color,toy_type):
        print('Закупается сырье для игрушки')
        self.purchase_materials(name)

        print('Начинается пошив игрушки')
        self.sew(name)

        print('Начинается покраска игрушки')
        self.paint(name)

        print('Игрушка готова!')
        return Toy(name,color,toy_type)

    def purchase_materials(self,name):
        print(f'Материалы для игрушки {name} закуплены!')

    def sew(self,name):
        print(f'Игрушка {name} сшита!')

    def paint(self,name):
        print(f'Игрушка {name} покрашена!')

factory = ToyFactory()
new_toy = factory.create_toy('Медвежонок', 'Коричневый', 'Животное')
print(new_toy)