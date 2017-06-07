#!/usr/bin/env python3

from gpiozero import Servo
from time import sleep

servo = Servo(17,
	min_pulse_width= 500/1000000,
	max_pulse_width=2400/1000000,
	frame_width    = 200/10000 #=20ms
)

print(servo.min_pulse_width)
print(servo.max_pulse_width)
print(servo.frame_width)
    
while True:
	servo.min()
	sleep(2)
	servo.max()
	sleep(2)
