#!/usr/bin/env python3

from gpiozero import LED

miled = LED(17) # crear un LED
miled.on()      # encenderlo


input("Pulsa una tecla para terminar ...") 