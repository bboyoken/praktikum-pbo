class Shop:
    def __init__(self, name):
        self.name = name

    def proses_pembelian(self, hero, item):
        if hero.gold >= item.harga:
            hero.gold -= item.harga
            print(f"{self.name} beli {item.name}"
                    f" {hero.name} sisa gold {hero.gold}")
            return True
        print(f"{self.name} Gold {hero.name} tidak cukup untuk {item.name}")
        return False

class Item:
    def __init__(self, name, harga, bonus_attack=0, bonus_armor=0):
        self.name = name
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor

    def __str__(self):
        return(f"Item {self.name} | +{self.bonus_attack} attack | +{self.bonus_armor} armor")

class Skill:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def __str__(self):
        return f"({self.name} {self.damage} damage, {self.mana_cost} mana)"

class Hero:
    jumlahHero = 0
    MAKS_SLOT = 4

    def __init__(self, name, health, mana, armor, attack, gold, list_skill):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self._inventory = []
        self._skills = [Skill(name, damage, mana) for name, damage, mana in list_skill]

    #penggunaan asosiasi
    def beli_item(self, shop, item):
        if len(self._inventory) >= self.MAKS_SLOT:
            print(f"Inventory {self.name} sudah penuh")
            return
        if shop.proses_pembelian(self, item):
            self._inventory.append(item)

    #agregasi
    def ambil_item(self, item):
        if len(self._inventory) < Hero.MAKS_SLOT:
            self._inventory.append(item)
            print(f"+ {self.name} mengambil {item.name}")

    #komposisi
    def cast_skill(self, nomor_skill, lawan):
        skill = self._skills[nomor_skill - 1]
        if self.mana < skill.mana_cost:
            print(f"Mana {self.name} tidak cukup untuk {skill.name} ")
            return
        self.mana -= skill.mana_cost
        lawan.health -= skill.damage
        print(f"{self.name} memakai {skill.name} ke {lawan.name}, "
                f"sisa health {lawan.name}: {lawan.health}")



brody = Hero(name="Brody", health=3000, mana=1000, armor=10, attack=100, gold=4000, list_skill=[("tembak",100,10), ("loncat", 10, 1)])
estes = Hero(name="Estes", health=3000, mana=1000, armor=10, attack=100, gold=4000, list_skill=[("tembak",100,10), ("loncat", 10, 1)])
shop = Shop("Belanja Item")
bod = Item("BOD", 3100, bonus_attack=160)
winter = Item("Winter", 2140, bonus_attack=15, bonus_armor=45)
brody.cast_skill(1, estes)

brody.beli_item(shop, bod)
brody.ambil_item(bod)
print()         