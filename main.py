import sys
from abc import abstractmethod


class Weapon:
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Боец делает выстрел из лука"

class AK74(Weapon):
    def attack(self):
        return "Боец даёт очередь из автомата"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError("Оружие должно быть экземпляром класса производного от Weapon.")
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

class Monster:
    def __init__(self, lifes=5):
        self.lifes = lifes

    def hit(self):
        self.lifes -= 1
        s = 'ь'
        if self.lifes >1: s = 'и'
        if self.lifes >0 :
            print(f"В меня попали, но у меня ещё есть {self.lifes} жизн{s}")
        else:
            print("О, - я убит!")
            print("Game over.")
            sys.exit()

    w = Sword()
    f = Fighter("Hero")
    f.change_weapon(w)
    m = Monster()
    f.attack()
    m.hit()

