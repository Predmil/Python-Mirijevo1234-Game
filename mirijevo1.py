import picking_place
import random
import mirijevo_template
from drawings import *
from clear import *

class Mirijevo1:
    def __init__(self):
        pass

    def greet(self):
        clearConsole()
        print("Добродошао у Миријево 1!")
        print("")
        print(mirijevo1)
        print("")
        print("Активности у Миријеву 1: ")
        print("")
        print("1) Иди у орловско насеље")
        print("2) Иди у седму")
        print("3) Иди код мартиновића")
        print("0) Иди назад")
        m1.pick()

    def pick(self):
        question = input("Где желиш да идеш?: ")
        while question not in ["1", "2", "3", "0"] or len(question) < 1:
            m1.greet()
        if question == "1":
            clearConsole()
            print("Кренуо си га орловском насељу!")
            m1.orlovsko()
        elif question == "2":
            clearConsole()
            print("Отишао си у седму!")
            m1.sedma()
        elif question == "3":
            clearConsole()
            print("Отишао си код другара!")
            m1.martinovic()
        elif question == "0":
            m1.nazad()


    def orlovsko(self):
        self.sit1 = "Срео си другара и шетали сте!"
        self.sit2 = "Нашао си енергетско пиће!"
        self.sit3 = "Ништа ниси нашао!"
        self.ran = random.choices([self.sit2, self.sit3, self.sit1])
        for x in self.ran:
            if "другара" in x:
                if mirijevo_template.t.health + 15 > 100:
                    pass
                else:
                    mirijevo_template.t.health += 15
                mirijevo_template.t.energy -= 5
                print("")
                print(f"{x} -----> | + 15HP | - 5 EN | ")
                mirijevo_template.t.show_stats()
            elif "енергетско" in x:
                mirijevo_template.t.health -= 15
                mirijevo_template.t.energy -= 5
                print("")
                print(f"{x} -----> | - 15HP | - 5 EN | ")
                mirijevo_template.t.show_stats()
            elif "Ништа" in x:
                mirijevo_template.t.energy -= 5
                print("")
                print(f"{x} -----> | + 0 HP | - 5 EN | ")
                mirijevo_template.t.show_stats()




    def sedma(self):
        self.nek1 = "Причао си са директором цео дан..."
        self.nek2 = "Срео си другаре из средње"
        self.nek3 = "Нема никога у седмој..."
        self.nek4 = "Звала те гага да једеш код ње за џабе"
        self.nek5 = "Посетио си професоре"
        self.take = random.choices([self.nek3, self.nek4, self.nek5, self.nek2, self.nek1])
        for x in self.take:
            if "директором" in x:
                clearConsole()
                print(x)
                mirijevo_template.t.health -= 3
                mirijevo_template.t.energy -= 6
                print("| - 3 HP | - 6 EN |")
                mirijevo_template.t.show_stats()
            elif "Срео" in x:
                clearConsole()
                print(x)
                if 100 - mirijevo_template.t.health < 4:
                    mirijevo_template.t.health += 100 - mirijevo_template.t.health
                else:
                    mirijevo_template.t.health += 4
                mirijevo_template.t.energy -= 4
                print("| + 4 HP | - 6 EN |")
                mirijevo_template.t.show_stats()
            elif "никога" in x:
                clearConsole()
                print(x)
                mirijevo_template.t.health += 0
                mirijevo_template.t.energy -= 2
                print("| + 0 HP | - 2 EN |")
                mirijevo_template.t.show_stats()
            elif "џабе" in x:
                clearConsole()
                print(x)
                if 100 - mirijevo_template.t.health < 7:
                    mirijevo_template.t.health += 100 - mirijevo_template.t.health
                else:
                    mirijevo_template.t.health += 7
                if 100 - mirijevo_template.t.energy < 3:
                    mirijevo_template.t.energy += 100 - mirijevo_template.t.energy
                else:
                    mirijevo_template.t.energy += 3
                print("| + 7 HP | + 3 EN |")
                mirijevo_template.t.show_stats()
            elif "професоре" in x:
                clearConsole()
                print(x)
                if 100 - mirijevo_template.t.health < 3:
                    mirijevo_template.t.health += 100 - mirijevo_template.t.health
                else:
                    mirijevo_template.t.health -= 3
                mirijevo_template.t.energy -= 3
                print("| + 3 HP | - 3 EN |")
                mirijevo_template.t.show_stats()


    def martinovic(self):
        clearConsole()
        print("Одрадили сте заједно тренинг")
        print("")
        if 100 - mirijevo_template.t.health < 7:
            mirijevo_template.t.health += 100 - mirijevo_template.t.health
        else:
            mirijevo_template.t.health += 30
        mirijevo_template.t.energy -= 4
        print("| + 7 HP | - 4 EN |")
        mirijevo_template.t.show_stats()




    def nazad(self):
        picking_place.p.celo_mrjv()


m1 = Mirijevo1()
