from pyshell.lexer import Lexer


def run(src_name, text):

    lexer = Lexer(src_name, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    NotImplemented


def main():
    instr = ""
    while not instr == "exit":
        instr = input("$MINISHELL >>> ")
        run("<stdin>", instr)


if __name__ == '__main__':
    main()
