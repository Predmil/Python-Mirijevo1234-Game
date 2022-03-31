import drawings
import mirijevo_template
from mirijevo1 import m1
from mirijevo2 import m2
from drawings import *
from clear import clearConsole
from drawings import celo_mirijevo
class Pick:
    def __init__(self):
        pass

    def celo_mrjv(self):
        clearConsole()
        print(celo_mirijevo)
        print("")
        print("| 1 | 2 | 3 | 4 | 0 - Назад |")
        ask = input("Изабери део Миријева: ")
        while ask not in ["1", "2", "3", "4", "0"] or len(ask) < 1:
            clearConsole()
            p.celo_mrjv()
        if ask == "1":
            clearConsole()
            m1.greet()

        elif ask == "2":
            clearConsole()
            m2.greet()

        elif ask == "3":
            p.celo_mrjv()

        elif ask == "4":
            p.celo_mrjv()

        elif ask == "0":
            clearConsole()
            mirijevo_template.t.show_stats()


    def pick(self):
        print(drawings.template)
        question = input("Где желиш да идеш?: ")
        while question not in ["1", "2", "3", "4"] or len(question) < 1:
            clearConsole()
            p.pick()
        if question == "1":
            clearConsole()
            print("Није довршени; Изабери 4")
            p.pick()
        if question == "2":
            clearConsole()
            print("Није довршени; Изабери 4")
            p.pick()
        if question == "3":
            clearConsole()
            print("Није довршени; Изабери 4")
            p.pick()
        if question == "4":
            clearConsole()
            p.celo_mrjv()








p = Pick()
