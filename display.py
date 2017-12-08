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

def processPK(key):
    global var
    var = False
    global string
    string = key

def processType(key):
    # Loop while waiting for a keypress
    global string
    if key == '*':
        string = string[:-1]
    else:
        string = string + key

def pinjam():
    lcd.cursor_pos = (0,0)
    lcd.write_string(u"Nomor Sepeda?")
    opt = keypad.registerKeyPressHandler(processType(key))
    while len(string) <= 4:
        time.sleep(0.1)
    no_sepeda = processType()
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string("Pnjm Spd " + no_sepeda + "?"))
    lcd.cursor_pos = (1,0)
    lcd.write_string("1:Ya 2:No")
    opt = keypad.registerKeyPressHandler(processPK(key)
    while var:
        time.sleep(0.1)
    print opt
    lcd.clear()
    if(string == 1):
        server_pinjam()
        lcd.cursor_pos = (0,0)
        lcd.write_string("Yay terpinjam")
        time.sleep(5)
    elif(string == 2):
        pass
    else:
        wrong_button()
        pinjam()

def wrong_button(text_up, text_down):
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string("Teken yg bener!")
    time.sleep(3)
    lcd.clear()
def kembali():
    server_kirim()
    
def wait_input(switch):
    while not GPIO.input(switch):
        time.sleep(0.01)

while True:
    lcd.cursor_pos = (0,0)
    lcd.write_string("Pinjam/Kembali?")
    lcd.cursor_pos = (1,0)
    lcd.write_string("1:P 2:K 3:Back")
    opt = keypad.registerKeyPressHandler(processPK)
    while var:
        time.sleep(0.1)
    lcd.clear()
    if(key == "1"):
        pinjam()
    elif (key == "2"):
        kembali()
    else:
        lcd.clear()
        lcd.write_string("Salah Pencet")
