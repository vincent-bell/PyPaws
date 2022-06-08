from pyshell.lexer import Lexer


def init_core_objects():
    return Lexer()


def main():
    lexer = init_core_objects()
    instr = ""
    while not instr == "exit":
        instr = input("$MINISHELL >>> ")
        tokens = lexer.make_tokens(instr)
        print(tokens)


if __name__ == '__main__':
    main()
