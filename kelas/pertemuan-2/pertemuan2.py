class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self._name = name
        self._health = health
        self._armor = armor
        self.attack = attack

    def __str__(self):
        return f'attack hero {self._name} = {self.attack}'  

    @property
    def getName(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def heroPower(self):
        return self._health + (self._armor * 1.5)


    @health.setter
    def health(self, darahBaru):
        if darahBaru <= 0:
            self._health = 0
        else:
            self._health = darahBaru

sniper = Hero('sniper', 100, 4, 15)
# print(sniper.armor)
print(sniper.getName)
print(sniper.__dict__)
sniper.health = 100
sniper.name = 'roger'
print(sniper.name)
# print(sniper.name)
# print(sniper.__dict__)
# print(sniper._Hero__name)
# print(sniper.health)