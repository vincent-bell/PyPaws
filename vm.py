from io import BytesIO
from libvm import int_to_bytes, int_from_bytes


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
