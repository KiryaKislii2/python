class MinStat:
    def __init__(self):
        self.re = []


    def add_number(self, num=int()):
        re1 = self.re
        re1.append(num)
        self.re = re1

    def result(self):
        if len(self.re) == 0:
            return None
        return min(self.re)



class MaxStat:
    def __init__(self):
        self.re = []


    def add_number(self, num=int()):
        re1 = self.re
        re1.append(num)
        self.re = re1

    def result(self):
        if len(self.re) == 0:
            return None
        return max(self.re)



class AverageStat:
    def __init__(self):
            self.re = []

    def add_number(self, num=int()):
        re1 = self.re
        re1.append(num)
        self.re = re1

    def result(self):
        if len(self.re) == 0:
            return None
        return (sum(self.re)) / len(self.re)