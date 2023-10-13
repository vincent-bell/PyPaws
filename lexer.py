class Lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.row = 0
        self.column = 0
        self.current = self.source[0]

        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"

    def make_tokens(self):

        while self.current:
            NotImplemented

        return self.tokens

    def advance(self):
        self.column += 1 if self.source[self.column] != "\n" else 0
        self.row += 1 if self.source[self.column] == "\n" else 0
        self.current = self.source[self.column] if self.column < len(self.source) else None


if __name__ == '__main__':
    source = """
    @import io

    output("Hello, World\n")
    """

    lexer = Lexer()
    print(lexer.make_tokens())
