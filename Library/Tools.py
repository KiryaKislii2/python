from CheckInfoBook import CheckInfoBook
from ChangeBook import ChangeBook
from book import book
from repair import repair
from load import load

def print_res(s):
    if type(s) == list:
        ch = 1
        for row in s:
            print(str(ch) + ')', str(row))
            ch += 1
    else:
        print(s)


def ready_book(id):
    return CheckInfoBook(id).result()

def change_book(ob=book):
    return ChangeBook(ob).result()

def repair_book(ob):
    return repair.parse(ob)

def save_book(ob, id):
    load.save(ob, id)



def menu():
    print('___________________________________________________________________________________')
    print('         __    __           __                     ')
    print(' |    * |__|  |__|    /\   |__|  \  /       Команды:')
    print(' |    | |   \ |  \   /__\  |  \   \/               <exit  --> выход             >')
    print(' |___ | |___/ |   \ /    \ |   \  /                <add   --> добавить книгу    >')
    print(' ________________________________/                 <print --> вывести все книги >')
    print('                                                   <del   --> удалить книгу     >')
    print('                                                   <srch  --> найти книгу       >')
    print('                                                   <ch    --> изменить книгу    >')
    print('  ')


def ex():
    print('___________________________________________________________________________________')
    print('  | |   | |       |   \ |___|  |   | / __  |___|    /\   |\  /|    ')
    print('  | |---| |---    |___/ |   \  |   | | | \ |   \   /__\  | \/ |                ')
    print('  | |   | |___    |     |    \ |___| |___/ |    \ /    \ |    |                    ')
    print('  ___  ___      ___   ___          ___        ___ _____  ___  ___    _        ')
    print('   |  /   \    /   \ |   | |\  /| |   | |    |      |   |    |   \  | |         ')
    print('   |  \___     |     |   | | \/ | |___| |    |___   |   |___ |    | | |       ')
    print('   |      \    |     |   | |    | |     |    |      |   |    |    | |/       ')
    print('  _|_ \___/    \___/ |___| |    | |     |___ |___   |   |___ |___/  o              ')
    print('___________________________________________________________________________________')
    print()



def search():
    print('___________________________________________________________________________________')
    print('                                          Команды:')
    print('                                                   <exit  --> выход             >')
    print('                                                   <name  --> поиск по имени    >')
    print('                                                   <auth  --> поиск по автору   >')
    print('                                                   <year  --> поиск по году     >')
    print('                                                   <art   --> поиск по артикулу >')