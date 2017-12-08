import SimpleMFRC522

import RPi.GPIO as GPIO
reader = SimpleMFRC522.SimpleMFRC522()

text = raw_input('New data:')
print("Now place your tag to write")
reader.write(text)
print("Written")