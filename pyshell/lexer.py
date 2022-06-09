from .errors import UnexpectedCharacterError
from .tokens import *
from .tracer import Position


DIGITS = "0123456789"


class Lexer:
    def __init__(self, src_name, text):
        self.src_name = src_name
        self.text = text
        self.position = Position(-1, 0, 1, src_name, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.position.advance(self.current_char)
        self.current_char = self.text[self.position.idx] if self.position.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:

            if self.current_char in " \t":
                self.advance()

            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == '+':
                tokens.append(Token(TOKEN_PLUS, start_pos=self.position))
                self.advance()

            elif self.current_char == '-':
                tokens.append(Token(TOKEN_MINUS, start_pos=self.position))
                self.advance()

            elif self.current_char == '*':
                tokens.append(Token(TOKEN_MULTIPLY, start_pos=self.position))
                self.advance()

            elif self.current_char == '/':
                tokens.append(Token(TOKEN_DIVIDE, start_pos=self.position))
                self.advance()

            elif self.current_char == '(':
                tokens.append(Token(TOKEN_LPAREN, start_pos=self.position))
                self.advance()

            elif self.current_char == ')':
                tokens.append(Token(TOKEN_RPAREN, start_pos=self.position))
                self.advance()

            else:
                start_pos = self.position.copy()
                echar = self.current_char
                self.advance()
                return None, UnexpectedCharacterError(start_pos, self.position, f'\'{echar}\'')

        tokens.append(Token(TOKEN_EOF, start_pos=self.position))
        return tokens, None

    def make_number(self):
        strnum = ""
        dot_count = 0
        start_pos = self.position.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count < 0:
                    break
                dot_count += 1
                strnum += '.'
            else:
                strnum += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOKEN_INT, int(strnum), start_pos, self.position)
        else:
            return Token(TOKEN_FLOAT, float(strnum), start_pos, self.position)
