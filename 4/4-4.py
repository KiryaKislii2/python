import datetime as d

class Date:
    
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        dt_1 = d.date(2022, self.month, self.day)
        dt_2 = d.date(2022, other.month, other.day)
        if dt_1 == dt_2:
            return 0
        return  ((str(dt_1 - dt_2)).split())[0]
        




mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
