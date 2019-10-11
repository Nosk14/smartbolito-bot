from neopixel import NeoPixel, RGB
import os
import board


NUM_LEDS = 50
leds = NeoPixel(board.D18, NUM_LEDS, auto_write=False, pixel_order=RGB, brightness=float(os.getenv("BRIGHTNESS", "0.2")))


def turn_off():
    leds.fill((0, 0, 0))
    leds.show()


def turn_on():
    set_color((255, 127, 0))


def set_color(color):
    leds.fill(color)
    leds.show()
