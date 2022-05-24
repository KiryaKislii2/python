from tkinter.messagebox import NO
from Library import Library
from Tools import print_res, menu, ex, repair_book, save_book
import json

def main():
    s = True
    try:
        with open('Stor.json') as file:
            xs = json.load(file)
    except:
        xs = None
    ch, mas = repair_book(xs)
    while s != False:
        a = Library(mas, ch)
        menu()
        x = str(input('Введите команду: ')).replace(' ', '')
        print('  ')
        if x == 'add':
            print('___________________________________________________________________________________')
            print_res(a.adde(ch))
            ch += 1
        elif x == 'print':
            print('___________________________________________________________________________________')
            print_res(a.show_dict())
        elif x == 'exit':
            s = False
            ex()
            save_book(a.mas, a.id)
        elif x == 'del':
            print('___________________________________________________________________________________')
            print(a.remove_book())
        elif x == 'srch':
            print('___________________________________________________________________________________')
            print_res(a.search_book())
        elif x == 'ch':
            print('___________________________________________________________________________________')
            print_res(a.change_book())
        else:
            print('___________________________________________________________________________________')
            print('Введеная команда не найдена!')


main()