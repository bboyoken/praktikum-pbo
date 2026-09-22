class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        Hero.jumlahHero += 1

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        print(f'{lawan.name} menerima serangan sebesar {self.attack}')

    def diserang(self, lawan, attack_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attack_lawan/self.armor
        self.health -= attack_diterima
        print(f'darah {self.name} tersisa {self.health}')

roger = Hero('roger', 100, 10, 15)
sniper = Hero('sniper', 80, 5, 20)

sniper.serang(roger)