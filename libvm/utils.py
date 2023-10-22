# bytecode -> registers
bytes_as_reg = {
    b'\x00': 'r0', b'\x01': 'r1', b'\x02': 'r2', b'\x03': 'r3',
    b'\x04': 'r4', b'\x05': 'r5', b'\x06': 'r6', b'\x07': 'r7',
    b'\x08': 'r8', b'\x09': 'r9', b'\x0a': 'pc'
}


# registers -> bytecode
register_as_bytes = {
    'r0': b'\x00', 'r1': b'\x01', 'r2': b'\x02',
    'r3': b'\x03', 'r4': b'\x04', 'r5': b'\x05',
    'r6': b'\x06', 'r7': b'\x07', 'r8': b'\x08',
    'r9': b'\x09', 'pc': b'\x0a'
}


# instructions -> bytecode
instruction_as_bytes = {
    'mov': b'\x00', 'inc': b'\x01', 'dec': b'\x02', 'add': b'\x03',
    'sub': b'\x04', 'mul': b'\x05', 'div': b'\x06', 'jmp': b'\x07',
    'cmp': b'\x08', 'jne': b'\x09', 'jeq': b'\x0a', 'jge': b'\x0b',
    'jgt': b'\x0c', 'jle': b'\x0d', 'jlt': b'\x0e', 'call': b'\x0f',
    'ret': b'\x10', 'syscall': b'\x11', 'end': b'\x12'
}


# instruction lengths (bytes)
instruction_length = {
    'mov': 4, 'inc': 2, 'dec': 2, 'add': 4,
    'sub': 4, 'mul': 4, 'div': 4, 'jmp': 4,
    'cmp': 5, 'jne': 3, 'jeq': 3, 'jge': 3,
    'jgt': 3, 'jle': 3, 'jlt': 3, 'prt': 3,
    'call': 3, 'ret': 1, 'end': 1
}


# syscalls -> bytecode
syscalls = {
    'PRINT': b'\x00', 'EXIT': b'\x01'
}
