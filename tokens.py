class Token:
    def __init__(self, _type, row, column, value=None):
        self.type = _type
        self.row = row
        self.column = column
        self.value = value


#####   Token types   #####

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

TT_EOF = 'EOF'
