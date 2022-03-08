class ReversedList:

    def __init__(self, lst=list()):
        self.orl = lst
        lst.reverse()


    def __len__(self):
        return len(self.orl)

    def __getitem__(self, key):
        return self.orl[key]



rl = ReversedList([10])
print(len(rl))
print(rl[0])