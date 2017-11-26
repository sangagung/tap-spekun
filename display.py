from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

from pad4pi import rpi_gpio

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

COL_PINS = [0,5,6,13] # BCM numbering
ROW_PINS = [19,26,20,21] # BCM numbering


factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])

def processPK(key):
    if (key=="1"):
        return 1
    elif (key=="2"):
        return 2
    elif (key=="3"):
        return 3
    else:
        return 0

def processType():
    # Loop while waiting for a keypress
    digitPressed = ""
    while len(digitPressed) < 4:
        digitPressed += keypad.getKey()
        lcd.cursor_pos(1,len(digitPressed))
        lcd.write_string(digitPressed)
    return digitPressed

def pinjam():
    lcd.cursor_pos(0,0)
    lcd.write_string(u"Nomor Sepeda?")
    no_sepeda = processType()
    lcd.clear()
    lcd.cursor_pos(0,0)
    lcd.write_string(u"Pnjm Spd " + no_sepeda + "?")
    lcd.cursor_pos(1,0)
    lcd.write_string(u"1:Ya 2:No 3:Back")
    opt = keypad.registerKeyPressHandler(processKey)
    lcd.clear()
    if(opt == 1):
        server_pinjam()
        lcd.cursor_pos(0,0)
        lcd.write_string(u"Yay terpinjam")
        time.sleep(5)
        return 1
    elif(opt == 2):
        return 2


while True:
    lcd.cursor_pos(0,0)
    lcd.write_string(u"Pinjam/Kembali?")
    lcd.cursor_pos(1,0)
    lcd.write_string(u"1:P 2:K 3:Back")
    option = keypad.registerKeyPressHandler(processKey)
    lcd.clear()
    if(option == 1):
        sukses_pinjam = 0
        while sukses_pinjam != 1
            sukses_pinjam = pinjam()