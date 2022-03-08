
class Date:
    def __init__(self, year, month, day):
        self.year = str(year)
        if len(str(month)) == 1:
            month = '0' + str(month)
        self.month = month
        if len(str(day)) == 1:
            day = '0' + str(day)
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        if len(str(month)) == 1:
            month = '0' + str(month)
        self.month = month

    def set_day(self, day):
        if len(str(day)) == 1:
            day = '0' + str(day)
        self.day = day

    def get_year(self):
        print(self.year)

    def get_month(self):
        print(self.month)

    def get_day(self):
        print (self.day)



class AmericanDate(Date):
    def format(self):
        return (str(self.month) + '.' + str(self.day) + '.' + str(self.year))



class EuropeanDate(Date):
    def format(self):
        return (str(self.day) + '.' + str(self.month) + '.' + str(self.year))


american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())

american.get_day()
american.get_month()
american.get_year()

american.set_day(7)
american.get_day()