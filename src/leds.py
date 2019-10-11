from neopixel import NeoPixel, RGB
import os
import board
import random
import time

NUM_LEDS = 50
leds = NeoPixel(board.D18, NUM_LEDS, auto_write=False, pixel_order=RGB,
                brightness=float(os.getenv("BRIGHTNESS", "0.2")))


def turn_off():
    leds.fill((0, 0, 0))
    leds.show()


def turn_on():
    set_color((255, 127, 0))


def set_color(color):
    leds.fill(color)
    leds.show()


def set_random_color():
    leds.fill((random.randrange(255), random.randrange(255), random.randrange(255)))
    leds.show()


def set_random_color_two():
    for i in range(0, 1000):
        leds.fill((random.randrange(255), random.randrange(255), random.randrange(255)))
        leds.show()
        time.sleep(0.5)


