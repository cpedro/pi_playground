#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""
File: blink.py
Description: Blinks an LED connected to GPIO pin 17 (WiringPi 0)
"""


__author__ = 'Chris Pedro'
__copyright__ = '(c) Chris Pedro 2021'
__licence__ = 'MIT'


import sys
import time
import wiringpi

from signal import signal, SIGINT


def main(args):
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(0, 1)
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        destroy()


def loop():
    wiringpi.digitalWrite(0, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(0, 0)
    time.sleep(0.5)


def destroy():
    wiringpi.digitalWrite(0, 0)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

