import random
class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        print('nama saya asep')
        Hero.jumlahHero += 1

    def healthUp(self, up):
        self.health = up

#     #instance method
#     def levelUp(self):
#         self.health += 50
#         self.armor += 5 
#         self.attack += 5

#     @classmethod
#     def totalhero(cls):
#         print(f'Total hero: {cls.jumlahHero}')

#     @staticmethod
#     def is_critical(peluang):
#         angka = random.randint(1, 100)
#         return angka < peluang

# roger = Hero('roger', 100, 10, 15)
# print(roger.name)
# print (roger.__dict__)
# roger.healthUp(150)
# sniper = Hero('sniper', 80, 5, 20)