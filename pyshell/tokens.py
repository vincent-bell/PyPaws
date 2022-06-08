####### TYPES ######~

TOKEN_ID = 'ID'
TOKEN_INT = 'INT'
TOKEN_FLOAT = 'FLOAT'


####### OPERATORS #######

TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MULTIPLY = 'MULTIPLY'
TOKEN_DIVIDE = 'DIVIDE'
TOKEN_EQUALS = 'EQUALS'


####### KEYWORDS #######

TOKEN_FUNC = 'FUNC'


####### MARKERS #######

TOKEN_COLON = 'COLON'
TOKEN_RARROW = 'RARROW'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_LBRACE = 'LBRACE'
TOKEN_RBRACE = 'RBRACE'
TOKEN_EOF = 'EOF'


####### TOKEN CLASS #######

class Token:
    def __init__(self, _type, value=None, start_pos=None, end_pos=None):
        self.type = _type
        self.value = value
        if start_pos:
            self.start_pos = start_pos.copy()
            self.end_pos = start_pos.copy()
            self.end_pos.advance()
        if end_pos:
            self.end_pos = end_pos

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
