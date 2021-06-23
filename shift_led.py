#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""
File: shift_led.py
Description: Uses 74CH559 shift register to blink a set of 8 LEDs.
"""


__author__ = 'Chris Pedro'
__copyright__ = '(c) Chris Pedro 2021'
__licence__ = 'MIT'


import sys
import time
import wiringpi
import utils


# Change to define output pins.  By default uses WiringPi 0, 2, 3.
clock_pin = 0
latch_pin = 2
data_pin = 3
pins = [clock_pin, latch_pin, data_pin]

time_delay = 0.5
loop_count = 0


def main(args):
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        destroy()


def update_shift_register(bit_order, leds):
    wiringpi.digitalWrite(latch_pin, wiringpi.LOW)
    wiringpi.shiftOut(data_pin, clock_pin, bit_order, leds)
    wiringpi.digitalWrite(latch_pin, wiringpi.HIGH)


def setup():
    wiringpi.wiringPiSetup()
    for pin in pins:
        wiringpi.pinMode(pin, wiringpi.OUTPUT)
    update_shift_register(wiringpi.LSBFIRST, int('0x00', 16))


def loop():
    # Alternate between LSB and MSB
    global loop_count
    loop_count += 1
    bit_order = wiringpi.LSBFIRST if loop_count % 2 else wiringpi.MSBFIRST

    # Start with clear LEDs
    leds = int('0x00', 16)
    # Loop through bits, setting each and updating the shift register.
    for i in range(8):
        leds = utils.set_bit(leds, i)
        update_shift_register(bit_order, leds)
        time.sleep(time_delay)


def destroy():
    update_shift_register(wiringpi.LSBFIRST, int('0x00', 16))
    for pin in pins:
        wiringpi.digitalWrite(pin, wiringpi.LOW)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
