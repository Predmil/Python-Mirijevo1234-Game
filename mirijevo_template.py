import xd
from picking_place import p
class Template:
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.money = 1000
        self.prijem = []
        self.inventar_has = []
        self.maxi_things = ["Кока Кола", "Чипс", "Чоколада", "Жваке", "Редбулл"]

    def show_stats(self):
        print(f"Име: {xd.game.name} | Паре: {self.money}")
        print("")
        print(f"Здравље:  |{self.health // 5 * '█'}{(20 - self.health // 5) * ' '}|---> {self.health}HP\n\n"
        f"Енергија: |{self.energy // 5 * '█'}{(20 - self.energy // 5) * ' '}|---> {self.energy}EN")
        p.pick()

t = Template()


