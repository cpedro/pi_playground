#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

def test_bit(data, offset):
    mask = 1 << offset
    return(data & mask)


def set_bit(data, offset):
    mask = 1 << offset
    return(data | mask)


def clear_bit(data, offset):
    mask = ~(1 << offset)
    return(data & mask)


def toggle_bit(data, offset):
    mask = 1 << offset
    return(data ^ mask)

