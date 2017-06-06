from gpiozero import LED

miled = LED(17) # crear un LED
miled.on()      # encenderlo




while True:
	# esperar
	print('hola')
