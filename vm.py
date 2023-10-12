from io import BytesIO
from libvm import int_to_bytes, int_from_bytes


# instructions -> bytecode
instruction_as_bytes = {
    'push': b'\x00', 'pop': b'\x01', 'mov': b'\x02',
    'inc': b'\x03', 'dec': b'\x04', 'add': b'\x05',
    'sub': b'\x06', 'mul': b'\x07', 'div': b'\x08',
    'jmp': b'\x09', 'cmp': b'\x0a', 'jne': b'\x0b',
    'jeq': b'\x0c', 'jge': b'\x0d', 'jgt': b'\x0e',
    'jle': b'\x0f', 'jlt': b'\x10', 'call': b'\x11',
    'ret': b'\x12', 'end': b'\x13'
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

    def run_program(self, bytecode):
        self.bytecode = bytecode
        current_instruction = self.bytecode.read(1)

        while current_instruction != b'\x13':
            self.exec(current_instruction)
            current_instruction = self.advance_byte()

    def advance_byte(self):
        self.increment_program_counter()
        self.bytecode.seek(int_from_bytes(self.pc.read(2)))
        return self.bytecode.read(1)

    def increment_program_counter(self):
        # TODO testing values > 255
        self.pc.seek(0)
        x = int_from_bytes(self.pc.read(2))
        x += 1
        self.pc.seek(0) if x > 255 else self.pc.seek(1)
        self.pc.write(int_to_bytes(x))
        self.pc.seek(0)

    def exec(self, instruction):
        NotImplemented
