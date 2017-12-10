from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

from pad4pi import rpi_gpio

flag = FALSE

pins_data=[18, 23, 24, 25]
pin_e=7
pin_rs=8

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_e, GPIO.OUT)
GPIO.setup(pin_rs, GPIO.OUT)
for pin in pins_data:
    GPIO.setup(pin, GPIO.OUT)

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

COL_PINS = [13,15,19,21] # BCM numbering
ROW_PINS = [3,5,7,11] # BCM numbering


factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

lcd = CharLCD(cols=16, rows=2, pin_rs=pin_rs, pin_e=pin_e, pins_data=pins_data, numbering_mode=GPIO.BCM)

global opt = keypad.registerKeyPressHandler(processPK)

global var
global string

def processPK(key):
    var = False
    global string
    string = key

def processType(key):
    # Loop while waiting for a keypress
    if key == '*':
        string = string[:-1]
    else:
        string = string + key

def pinjam():
    print("nomor sepeda?")
    opt = keypad.registerKeyPressHandler(processType(key))
    while len(string) <= 4:
        time.sleep(0.1)
    no_sepeda = string
    print("Pnjm Spd " + no_sepeda + "?"))
    print("1:Ya 2:No")
    
    opt = keypad.registerKeyPressHandler(processPK(key))
    var = True
    while var:
        time.sleep(0.1)
    print("anda memilih sepeda" + string)
    if(string == 1):
        print("Yay terpinjam")
    elif(string == 2):
        pass
    else:
        pinjam()

def wrong_button(text_up, text_down):
    print("Teken yg bener!")

def kembali():
    server_kirim()
    print("terima kasih telah mengembalikan!")

def wait_input(switch):
    while not GPIO.input(switch):
        time.sleep(0.01)

while True:
    print("Pinjam/Kembali?")
    print("1:P 2:K 3:Back")
    opt = keypad.registerKeyPressHandler(processPK)
    var = True
    while var:
        time.sleep(0.1)

    if(string == "1"):
        pinjam()
    elif (string == "2"):
        kembali()
    else:
        print("Salah Pencet")