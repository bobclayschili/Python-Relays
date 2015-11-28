#!/usr/bin/python
# coding=UTF-8
from pylibftdi import BitBangDevice
import sys, time
def relay_on(relay):
        with BitBangDevice() as bb:
            bb.port |= relay

def relay_off(relay):
        with BitBangDevice() as bb:
            bb.port &= ~relay
# it counts in binary. 1,2,3,4,5,6 would be 1,2,4,8,16,32,etc.
for i in range(1,9):
    relay_on(i)
    time.sleep(.5)
    relay_off(i)
sys.exit(0)


