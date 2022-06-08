from .tracer import Position


class Lexer:
    def __init__(self, src_name, text):
        self.src_name = src_name
        self.text = text
        self.position = Position(-1, 0, 1, src_name, text)
        self.current_char = None
        self.advance()
        
    def make_tokens(self):
        NotImplemented
