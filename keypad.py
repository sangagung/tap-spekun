from pad4pi import rpi_gpio
import time

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

ROW_PINS = [4, 14, 15, 17] # BCM numbering
COL_PINS = [18, 24, 22, 23] # BCM numbering

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
    print(key)

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

while True:
	time.sleep(0.7)
	pass

keypad.cleanup()
