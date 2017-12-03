from RPLCD import CharLCD
import RPI.GPIO as GPIO
import time

from pad4pi import rpi_gpio

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

lcd = CharLCD(cols=16, rows=2, pin_rs=2, pin_e=6, pins_data=[26, 24, 22, 18, 16, 12, 2, 4])

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
    lcd.write_string("Pnjm Spd " + no_sepeda + "?")
    lcd.cursor_pos(1,0)
    lcd.write_string("1:Ya 2:No")
    opt = keypad.registerKeyPressHandler(processKey)
    lcd.clear()
    if(opt == 1):
        server_pinjam()
        lcd.cursor_pos(0,0)
        lcd.write_string("Yay terpinjam")
        time.sleep(5)
    elif(opt == 2):
        opt = pinjam()
    else:
        wrong_button("Pnjm Spd " + no_sepeda + "?", "1:Ya 2:No")
        opt = pinjam()
    return opt

def wrong_button(text_up, text_down):
    lcd.clear()
    lcd.cursor_pos(0,0)
    lcd.write_string("Teken yg bener!")
    time.sleep(3)
    lcd.clear()
    lcd.cursor_pos(0,0)
    lcd.write_string(text_up)
    lcd.cursor_pos(1,0)
    lcd.write_string(text_down)

def kembali():
    server_kirim()
    
def wait_input(switch):
    while not GPIO.input(switch):
        time.sleep(0.01)

while True:
    lcd.cursor_pos(0,0)
    lcd.write_string("Pinjam/Kembali?")
    lcd.cursor_pos(1,0)
    lcd.write_string("1:P 2:K 3:Back")
    option = keypad.registerKeyPressHandler(processKey)
    lcd.clear()
    if(option == 1):
        pinjam()
    elif (option == 2):
        kembali()
    else:
        lcd.clear()
        lcd.write_string("Salah Pencet")