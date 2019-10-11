import time
from leds import leds


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
    time.sleep(milis/1000.0)


def led_operation(param):
    for i, c in enumerate(param.upper()):
        leds[i] = COLORS[c]
    leds.show()


def tag_operation(param):
    pass


def jump_operation(param):
    pass


OPERATIONS = {
    "WAIT": wait_operation,
    "LED": led_operation,
    "TAG": tag_operation,
    "JUMP": jump_operation
}


class Program:

    def __init__(self):
        pass
