import picking_place
import random
import mirijevo_template
from drawings import *
from clear import *

class Mirijevo2:
    def __init__(self):
        pass

    def greet(self):
        clearConsole()
        print("Добродошао у Миријево 2!")
        print("\n")
        print(mirijevo2)
        print("\n")
        print("Активности у Миријеву 2: ")
        print("")
        print("1) Иди у главну пошту")
        print("2) Иди код Василија")
        print("3) Иди у макси")
        print("4) Иди у ахилеј")
        print("5) Иди у амстердам")
        print("0) Иди назад")
        m2.pick()

    def pick(self):
        question = input("Где желиш да идеш?: ")
        while question not in ["1", "2", "3", "4", "5", "0"] or len(question) < 1:
            m2.greet()
        if question == "1":
            clearConsole()
            m2.posta()
        elif question == "2":
            m2.sova()
        elif question == "3":
            clearConsole()
            m2.maxi()
        elif question == "4":
            clearConsole()
            m2.ahilej()
        elif question == "5":
            clearConsole()
            m2.amsterdam()
        elif question == "0":
            clearConsole()
            picking_place.p.celo_mrjv()

    def posta(self):
        if len(mirijevo_template.t.prijem) < 1:
            print("Тренутно немате никакав пријем робе")
        else:
            print("Молимо вас да покупите вашу робу")
            for thing in mirijevo_template.t.prijem:
                print(f"{thing} ----> на стању")

    def sova(self):
        clearConsole()
        self.a = "Отишао си код другара кући и играли сони"
        self.b = "Задесио си се на журци и попио пиво"
        self.c = "Играо си монопол са другаром"
        self.chance = random.choices([self.c, self.a, self.b])
        for x in self.chance:
            if "другара" in x:
                clearConsole()
                print(x)
                mirijevo_template.t.money -= 500
                if 100 - mirijevo_template.t.health < 7:
                    mirijevo_template.t.health += 100 - mirijevo_template.t.health
                else:
                    mirijevo_template.t.health += 7

                if 100 - mirijevo_template.t.energy < 4:
                    mirijevo_template.t.energy += 100 - mirijevo_template.t.energy
                else:
                    mirijevo_template.t.energy += 4
                print("| + 7 HP | + 4 EN | -500 DINARA |")
                mirijevo_template.t.show_stats()
            elif "касно" in x:
                clearConsole()
                print(x)
                print(pivo)
                print("\n")
                mirijevo_template.t.health -= 15
                mirijevo_template.t.energy -= 5
                mirijevo_template.t.money -= 200
                print("| - 15 HP | - 5 EN | -200 DINARA |")
                mirijevo_template.t.show_stats()
            elif "монопол" in x:
                clearConsole()
                print(x)
                if 100 - mirijevo_template.t.health < 7:
                    mirijevo_template.t.health += 100 - mirijevo_template.t.health
                else:
                    mirijevo_template.t.health += 7

                if 100 - mirijevo_template.t.energy < 4:
                    mirijevo_template.t.energy += 100 - mirijevo_template.t.energy
                else:
                    mirijevo_template.t.energy += 4
                print("| + 7 HP | + 4 EN |")
                mirijevo_template.t.show_stats()




    def maxi(self):
        clearConsole()
        print("Добродошао у макси!")
        print("\n")
        print("Ствари које су ти у ранцу: ")
        if len(mirijevo_template.t.inventar_has) < 1:
            print("Ранац ти је празан!")
        else:
            for x in mirijevo_template.t.inventar_has:
                print(x)
        print("\n")
        print("Тренутно на располагању:")
        if len(mirijevo_template.t.maxi_things) < 1:
            print("Нема више ствари у максију!")
            print("\n")
            question = input("Укуцај 0 да се вратиш назад: ")
            while question != "0":
                m2.maxi()
            if question == "0":
                m2.greet()

        else:
            for number, thing in enumerate(mirijevo_template.t.maxi_things, start=1):
                if thing == "Кока Кола":
                    print(f"{number}: {thing} ---> на распологању | Цена ---> 80 ДИН")
                elif thing == "Чипс":
                    print(f"{number}: {thing} ---> на распологању | Цена ---> 60 ДИН")
                elif thing == "Чоколада":
                    print(f"{number}: {thing} ---> на распологању | Цена ---> 350 ДИН")
                elif thing == "Жваке":
                    print(f"{number}: {thing} ---> на распологању | Цена ---> 50 ДИН")
                elif thing == "Редбулл":
                    print(f"{number}: {thing} ---> на распологању | Цена ---> 150 ДИН")
            print("0: Ништа ---> Изаћи из максија")
            print("\n")
            question = input("Шта купујеш?: ")
            if question == "0":
                clearConsole()
                m2.greet()
            elif len(question) < 1:
                m2.maxi()
            elif int(question) not in range(len(mirijevo_template.t.maxi_things)+1):
                m2.maxi()
            elif int(question) in range(len(mirijevo_template.t.maxi_things)+1):
                for number, thing in enumerate(mirijevo_template.t.maxi_things):
                    if int(question) == number + 1:
                        clearConsole()
                        if thing == "Кока Кола":
                            clearConsole()
                            mirijevo_template.t.money -= 80
                            print("Купио си кока колу! | -80 ДИН |")
                            mirijevo_template.t.inventar_has.append(thing)
                            mirijevo_template.t.maxi_things.pop(int(question) - 1)
                            m2.maxi()
                        elif thing == "Чипс":
                            clearConsole()
                            print("Купио си чипс! | -60 ДИН |")
                            mirijevo_template.t.money -= 60
                            mirijevo_template.t.inventar_has.append(thing)
                            mirijevo_template.t.maxi_things.pop(int(question) - 1)
                            m2.maxi()
                        elif thing == "Чоколада":
                            clearConsole()
                            print("Kupio si чоколаду! | -350 ДИН |")
                            mirijevo_template.t.money -= 350
                            mirijevo_template.t.inventar_has.append(thing)
                            mirijevo_template.t.maxi_things.pop(int(question) - 1)
                            m2.maxi()
                        elif thing == "Жваке":
                            clearConsole()
                            print("Купио си жваке! | -50 ДИН |")
                            mirijevo_template.t.money -= 50
                            mirijevo_template.t.inventar_has.append(thing)
                            mirijevo_template.t.maxi_things.pop(int(question) - 1)
                            m2.maxi()
                        elif thing == "Редбулл":
                            clearConsole()
                            print("Купио си редбулл! | -150 ДИН |")
                            mirijevo_template.t.money -= 150
                            mirijevo_template.t.inventar_has.append(thing)
                            mirijevo_template.t.maxi_things.pop(int(question) - 1)
                            m2.maxi()






    def ahilej(self):
        m2.greet()

    def amsterdam(self):
        m2.greet()

    def nazad(self):
        m2.greet()

m2 = Mirijevo2()