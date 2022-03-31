import time
from clear import clearConsole
from mirijevo_template import t
class Mirijevo:

    def __init__(self, name):
        self.name = name
        while len(self.name) < 4:
            print("Име мора да има више од 3 слова!")
            self.name = input("Изабери име: ")


    def greeting(self):
        pos = ["y", "yes", "ye","Д", "Да", "d", "da", "да"]
        neg = ["no", "n", "Н", "Не", "ne", "не"]
        clearConsole()
        print(f"Hello {self.name}!")
        question = input("Да ли си сигуран да желиш да наставиш?\n"
                         "Одговори овде: ")
        while question.lower() not in pos and question.lower() not in neg:
            question = input("Погрешан одговор, пробај поново: ")
        if question.lower() in pos:
            clearConsole()
            print("Почео си са игром!")
            game.show()
        elif question.lower() in neg:
            print("Напушташ аутобус!")
            exit(Mirijevo)




    def show(self):
        time.sleep(1)
        print("Добродошао у Миријево!\n"
              "Твој задатак ће бити да се упознаш са градом!\n ")
        t.show_stats()



game = Mirijevo(input("Упиши своје име...\nУкуцај овде: "))
game.greeting()



