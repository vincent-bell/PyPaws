def string_with_arrows(text, pos_start, pos_end):
    result = ''

    index_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    index_end = text.find('\n', index_start + 1)
    if index_end < 0: index_end = len(text)

    line_count = pos_end.row - pos_start.row + 1
    for i in range(line_count):
        line = text[index_start:index_end]
        col_start = pos_start.column if i == 0 else 0
        col_end = pos_end.column if i == line_count - 1 else len(line) - 1

        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        index_start = index_end
        index_end = text.find('\n', index_start + 1)
        if index_end < 0: index_end = len(text)

    return result.replace('\t', '')


class Error:
    def __init__(self, start_pos, end_pos, error_name, details):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.error_name = error_name
        self.details = details

    def __repr__(self):
        return f'{self.error_name}: {self.details}\n' + f'''
        File {self.start_pos.src_name}, line {self.start_pos.column + 1}
        \n\n''' + string_with_arrows(self.start_pos.text, self.start_pos, self.end_pos)

class UnexpectedCharacterError(Error):
    def __init__(self, start_pos, end_pos, details):
        super().__init__(start_pos, end_pos, "Unexpected Character", details)
