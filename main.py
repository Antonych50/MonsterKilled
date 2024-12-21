import sys
from abc import abstractmethod
from abc import ABC

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Наносит удар мечом"

    def str(self):
        return "Меч"


class Bow(Weapon):
    def attack(self):
        return "Делает выстрел из лука"

    def str(self):
        return "Лук"

class AK74(Weapon):
    def attack(self):
        return "Даёт очередь из автомата"

    def str(self):
        return "AK74"


class Fighter:
    weapon =None
    def __init__(self, name):
        self.name = name

    def change_weapon(self, weapon: Weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError("Оружие должно быть экземпляром класса производного от Weapon.")
        else:
            self.weapon = weapon
            print(f"{self.name} выбрал {self.weapon.str()}")

    def attack(self):
        return self.name +": " +self.weapon.attack()

class Monster():
    n = 0 #число жизней
    def __init__(self, n = 5):
        self.n = n

    def hit(self):
        self.n -= 1
        s = 'ь'
        if self.n >1: s = 'и'
        if self.n >0 :
            print(f"Монстр: 'В меня попали, но у меня ещё есть {self.n} жизн{s}'")
        else:
            print("Монстр: 'О-o-o, - я убит!'")
            print("Game over.")
            sys.exit()

w = Sword()
f = Fighter("Hero")
f.change_weapon(w)
m = Monster(3)
print(f.attack())
m.hit()
w = AK74()
f.change_weapon(w)
print(f.attack())
m.hit()
print(f.attack())
m.hit()
