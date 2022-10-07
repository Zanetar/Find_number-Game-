from random import *
import random
class Game:
    def __int__(self,name,level):
        self.name=name
        self.level=level

class Find_number(Game):
    def __int__(self, name,level,age):
        super().__init__(name,level,age)

    def __repr__(self):
        return('Gra znajdź liczbę. Dowiedz się jaką cyfrę wylosował komputer')
    def rules(self):
        print('Witaj w grze')
        print ('Za chwile komputer wylosuje liczbę całkowitą z zakresu 1-100.')
        print('Twoim zadaniem jest odgadnięcie tej właśnie liczby')
        print('Sam decydujesz ile prób potrzeba Ci na jej odgadnięcie')


    def choose(self):
        while True:
            try:
                choose=int(input('Wpisz liczbę prób z zakresu od 1-10, lub 0 aby przerwać'))
                if choose >=1 and choose<=10:
                    print(f'Twoja liczba prób to {choose} razy')
                    break
                    return choose
                elif choose== 0:
                    break
            except: print('Wprowadzono zły znak!')
        return choose

    def game(self,object):
        number= randint(1, 100)
        start=object.choose()
        while True:
            if start==0:
                print('Gra przerwana!')
                break
            try:
                players_number = int(input('Wprowadź swoją propzycję'))
                print(f'pozostało Ci {start} żyć')
                start = start - 1
                if number ==players_number:
                    print('wygrałeś!')
                    break
                elif number >players_number:
                    print('wylosowana liczba jest większa')
                    if start <= 0:
                        print('przegrałeś')
                        break
                elif number < players_number:
                    print('wylosowana liczba jest mniejsza')
                    if start == 0:
                        print('przegrałeś')
                        break
            except: print ('Wybrano zły znak!')


    def end(self):
        try:
            print('Czy chcesz grać dalej? Tak-1, Nie-0')
            anwser=int(input())
            if anwser==1 or anwser==0:
                return anwser
            else:
                print('Wybrałeś zły znak')
        except:
            print('Wybrałeś zły znak')

def menu_find(object):
    while True:
        object.rules()
        if object.game(object)==0:
            print('Do widzenia!')
            break
        else:
            if object.end()==0:
                print('Do widzenia!')
                break

second_game=Find_number()

menu_find(second_game) #uruchomienie programu
