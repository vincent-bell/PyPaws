from io import BytesIO
from libvm import int_to_bytes, int_from_bytes


# instructions -> bytecode
instruction_as_bytes = {
    'mov': b'\x00', 'inc': b'\x01', 'dec': b'\x02', 'add': b'\x03',
    'sub': b'\x04', 'mul': b'\x05', 'div': b'\x06', 'jmp': b'\x07',
    'cmp': b'\x08', 'jne': b'\x09', 'jeq': b'\x0a', 'jge': b'\x0b',
    'jgt': b'\x0c', 'jle': b'\x0d', 'jlt': b'\x0e', 'call': b'\x0f',
    'ret': b'\x10', 'syscall': b'\x11', 'end': b'\x12'
}


# syscalls -> bytecode
syscalls = {
    'PRINT': b'\x00', 'EXIT': b'\x01'
}


class VirtualMachine:
    def __init__(self):
        self.__registers = {
            'r0', 'r1', 'r2', 'r3', 'r4',
            'r5', 'r6', 'r7', 'r8', 'r9',
            'pc'
        }
        self.__registers['pc'] = BytesIO(b'\x00\x00')
        self.flags = { 'zf': False, 'sf': False }
        self.call_stack = []

    def registers(self):
        return self.__registers

    def run_program(self, bytecode):
        self.bytecode = bytecode
        current_instruction = self.bytecode.read(1)

        while current_instruction != b'\x13':
            self.exec(current_instruction)
            current_instruction = self.advance_byte()

    def advance_byte(self):
        self.increment_program_counter()
        self.bytecode.seek(int_from_bytes(self.registers['pc'].read(2)))
        return self.bytecode.read(1)

    def increment_program_counter(self):
        # TODO testing values > 255
        self.pc.seek(0)
        x = int_from_bytes(self.registers['pc'].read(2))
        x += 1
        self.registers['pc'].seek(0) if x > 255 else self.registers['pc'].seek(1)
        self.registers['pc'].write(int_to_bytes(x))
        self.registers['pc'].seek(0)

    def exec(self, instruction):
        NotImplemented
