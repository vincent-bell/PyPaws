import re


class Assembler:
    def __init__(self):
        self.write_offset = 0
        self.labels = {}

    def preprocess(self):
        NotImplemented

    def assemble(self, source):
        NotImplemented

    def write_register(self, register):
        NotImplemented

    def write_immediate(self, value):
        NotImplemented

    def make_le_pointer(self, value):
        NotImplemented

    def parse_command(command):
        matches = re.findall(r"\w+|'.*?'", command)
        return matches[0], matches[1:]


if __name__ == '__main__':
    source = """
    .paws                              // smart assembly for paws virtual machine
    .text                              // text section

    _main:                             // entry point
        mov r0, #5                     // store 16-bit signed integer 5 in r0
        mov r1, #10                    // store 16-bit signed integer 10 in r1
        add r0, r0, r1                 // add r0 and r1 and store in r0
        mov r1, @(addr)
        syscall PRINT                  // invoke PRINT syscall ~ PRINT handles null-terminated strings, use PRINTS for non-null-terminated strings
        mov r0, #0                     // store 16-bit signed integer 0 in r0 for exit status
        syscall EXIT                   // exit program

    .data                              // data section
        addr: 0xYYYYYYYY               // address of null-terminated string
    """
    assembler = Assembler()
    assembler.assemble(source)
