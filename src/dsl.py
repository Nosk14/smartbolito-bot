from threading import Thread
from leds import leds
import time

COLORS = {
    'X': (0, 0, 0),
    'R': (255, 0, 0),
    'G': (0, 255, 0),
    'B': (0, 0, 255),
    'W': (255, 255, 255),
    'Y': (255, 255, 0),
    'O': (255, 127, 0),
    'P': (255, 0, 255)
}


def wait_operation(param):
    milis = int(param)
    time.sleep(milis / 1000.0)


def led_operation(param):
    for i, c in enumerate(param):
        leds[i] = COLORS[c]
    leds.show()


def jump_operation(param, program):
    program.pc = program.tags[param]


OPERATIONS = {
    "WAIT": wait_operation,
    "LED": led_operation,
    "JUMP": jump_operation
}


class Program(Thread):

    def __init__(self, raw_program):
        super().__init__()
        self.__continue = True
        self.__program_instructions = []
        self.tags = {}
        self.pc = 0
        self.__parse_program(raw_program.strip().upper().split('\n'))

    def stop(self):
        self.__continue = False

    def __parse_program(self, program_lines):
        i = 0
        for line in program_lines:
            if line:
                operation, params = line.strip().split(maxsplit=1)
                if operation == "TAG":
                    self.tags[params] = i - 1
                else:
                    self.__program_instructions.append((OPERATIONS[operation], params))
                    i += 1

    def run(self):
        while self.__continue and self.pc < len(self.__program_instructions):
            instruction, params = self.__program_instructions[self.pc]
            instruction(params)
            self.pc += 1

