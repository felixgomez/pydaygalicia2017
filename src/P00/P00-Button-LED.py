#!/usr/bin/env python3

from gpiozero import LED, Button

miled = LED(17)      # crear un LED
miboton = Button(2)  # crear un pulsador

while True:
	if miboton.is_pressed:
		miled.on()
	else:
		miled.off()
