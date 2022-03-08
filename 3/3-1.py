class LeftParagraph:
    
    def __init__(self, ch=int()):
        self.ch = ch
        self.x = []

    def add_word(self, st=str()):

        if len(self.x) == 0 or len(st + self.x[-1]) >= self.ch:
            self.x.append(st)
        else:
            self.x[-1] = self.x[-1] + ' ' + str(st)
            

    def end(self):
        for x in self.x:
            print(x)



class RightParagraph:
    
    def __init__(self, ch=int()):
        self.ch = ch
        self.x = []

    def add_word(self, st=str()):

        if len(self.x) == 0 or len(st + (self.x[-1]).lstrip()) >= self.ch:
            self.x.append(st.rjust(self.ch, ' '))
            
            
        else:
            self.x[-1] = (self.x[-1].lstrip() + ' ' + str(st)).rjust(self.ch, ' ')
            

    def end(self):
        for x in self.x:
            print(x)



rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
