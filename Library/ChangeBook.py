from book import book

class ChangeBook:
    def __init__(self, old_book=book):
        self.old_book = old_book

        self.name = input(f'Введите название(или оставить "{self.old_book.get_name()}"):  ')
        self.ch_name()

        self.author = input(f'Введите автора(или оставить "{self.old_book.get_author()}"):  ')
        self.ch_author()

        self.year = input(f'ВВведите год(или оставить "{self.old_book.get_year()}"):  ')
        self.ch_year()

        self.number = input(f'Введите артикул(или оставить "{self.old_book.get_number()}"):  ')
        self.ch_number()

    def ch_name(self):
        if self.name != '':
            self.old_book.set_name(self.name)
        

    def ch_author(self):
        if self.author != '':
            while (self.author.replace(' ', '') == '') or (self.author.isnumeric() == True):
                if self.author.replace(' ', '') == '':
                    print('\nERROR: Книга не может быть без автора!')
                    print('___________________________________________________________________________________')
                if (self.author.isnumeric() == True):
                    print('\nERROR: Книга не может быть цифрой!')
                    print('___________________________________________________________________________________')
                    self.author = input('Введите автора:  ')
            self.old_book.set_author(self.author)


    def ch_year(self):
        if self.year != '':
            try:
                self.old_book.set_year(int(self.year))
            except:     
                while (not isinstance(self.year, int)) or (str(self.year).replace(' ', '')):
                    
                    print('\nERROR: Книга не может быть без года издания или строкой, введите число!')  
                    print('___________________________________________________________________________________')      
                    try:
                        self.old_book.set_year(int(input('Введите год издания:  ')))
                        break
                    except:
                        pass

    def ch_number(self):
        if self.number != '':
            self.old_book.set_number(self.number)


    def result(self):
        return self.old_book

