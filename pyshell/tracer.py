class Position:
    def __init__(self, idx, row, column, src_name, text):
        self.idx = idx
        self.row = row
        self.column = column
        self.src_name = src_name
        self.text = text

    def __repr__(self):
        return f'Position({self.idx}, {self.row}, {self.column}, {self.src_name}, \"{self.text}\")'

    def advance(self, current_char=None):
        self.idx += 1
        self.column += 1
        if current_char == '\n':
            self.row += 1
            self.column = 0
        return self

    def copy(self):
        return Position(self.idx, self.row, self.column, self.src_name, self.text)
