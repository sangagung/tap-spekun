import SimpleMFRC522

import RPi.GPIO as GPIO
reader = SimpleMFRC522.SimpleMFRC522()

text = raw_input('New data:')
print("Now place your tag to write")
reader.write(text)
print("Written")


with open('/dev/tty0', 'r') as tty:
    while True:
        byte = tty.read(1)
        counter = 0
        while byte != "":
            # Do stuff with byte.
            byte = f.read(1)
            
            counter += 1