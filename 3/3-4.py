class Table:

    def __init__(self, rows=int(), cols=int()):
        self.rows = rows
        self.cols = cols
        tabl = []
        d = '0 ' * cols
        s = list(map(lambda x: int(x), d.split()))
        for i in range(cols):
            tabl.append(s.copy())
        self.tabl = tabl


    def get_value(self, row, col):
        if int(row) > self.rows or int(col) > self.cols:
            return None
        else:
            tabl = self.tabl
            return tabl[int(row)][int(col)]

    def set_value(self, row, col, value):
            tabl = self.tabl

            tabl[int(row)][int(col)] = int(value)
            self.tabl = tabl

    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols