#!/usr/bin/env python3
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep
from random import choice
import os

BUMP_PROX = 50
FWD_SPEED = -50
BWD_SPEED = 50
AVOID_FWD_SPEED = -100
AVOID_BWD_SPEED = 100

def turn_left_or_right():
    return choice([
        [AVOID_FWD_SPEED, AVOID_BWD_SPEED],
        [AVOID_BWD_SPEED, AVOID_FWD_SPEED]
    ])

#
# Simple Python script to have the EV3D4 move around
# and avoid bumping into things
os.system('setfont Lat15-TerminusBold14')
leds = Leds()
leds.all_off()
ts = TouchSensor()
ir = InfraredSensor()

print("Waiting to go!  Press the sensor.")
leds.animate_cycle(('RED', 'GREEN', 'AMBER'), block=False)
while not ts.is_pressed:
    sleep(0.1)
leds.animate_stop()

print("Going for a walk ...")
leds.animate_rainbow(block=False)

mt = MoveTank(OUTPUT_B, OUTPUT_C)
while not ts.is_pressed:
    mt.on(left_speed=FWD_SPEED, right_speed=FWD_SPEED)
    sleep(0.5)
    if (ir.proximity < BUMP_PROX):
        mt.off()
        mt.on_for_seconds(left_speed=BWD_SPEED, right_speed=BWD_SPEED, seconds=1)
        avoid_speeds = turn_left_or_right()
        mt.on_for_seconds(left_speed=avoid_speeds[0], right_speed=avoid_speeds[1], seconds=0.75)

mt.off()
leds.animate_stop()
print("Done ...")
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'GREEN')
sleep(5)
print("Back to sleep!")
leds.all_off()



