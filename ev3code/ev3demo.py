#!/usr/bin/env python3
from ev3dev2 import sound
import os
os.system('setfont Lat15-TerminusBold14')
print('Hello, my name is EV3D4!')
sound = sound.Sound()
sound.speak('Hello, my name is EV3D4')
