import sphero
import time
import random

def getSpheroObject():
    s=sphero.core.Sphero()
    return s


def hex_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def changeColor(s,hexColor):
    color=hex_to_rgb(hexColor)
    s.connect()
    s.set_rgb(color[0],color[1],color[2])
    return


def roll(s,distance,angle):
    s.connect()
    s.roll(100,angle)
    return

def stop(s):
    s.connect()
    s.roll(0,0)
    return

def showHeadLight(s,flag):
    s.connect()
    if flag:
        s.set_back_led_output(0xFF)
    else:
        s.set_back_led_output(0x00)
