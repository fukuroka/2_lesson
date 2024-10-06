class Person:
    def __init__(self,health,damage,armor,name):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def attack(self,unit):
        unit.health -= self.__get_damage(unit)
        unit.health = max(0,unit.health)
        print(f'{self.name} атакует {unit.name}! У {unit.name} осталось {unit.health} HP!\n')

    def __get_damage(self,unit):
        return self.damage * (1-(round(unit.armor/100, 2)))


class Player(Person):
    def __init__(self,health,damage,armor,name):
        super().__init__(health,damage,armor,name)
        self.level = 1

    def level_up(self):
        self.health += self.health*0.1
        self.armor += self.armor * 0.1
        self.damage += self.damage * 0.1
        self.level += 1

        print(f'{self.name} повысил уровень! Теперь у него {self.level} уровень, все показатели возрасли на 10%!')

class Enemy(Person):
    def __init__(self,health,damage,armor,name):
        super().__init__(health,damage,armor,name)

class Game:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy

    def start_game(self):

        while self.player.health >0 and self.enemy.health >0:
            self.player.attack(self.enemy)

            if self.enemy.health <= 0:
                print(f'{self.player.name} победил!')
                self.player.level_up()
                break
            self.enemy.attack(self.player)

            if self.player.health <= 0:
                print(f'{self.enemy.name} победил!')
                break


p1 = Player(200,20,10,'Добряк')
p2 = Enemy(150,25,10,'Злодей злодейский')
game = Game(p1,p2)
game.start_game()

