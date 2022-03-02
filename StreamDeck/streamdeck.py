import machine
import utime
import keyboard

button = machine.Pin(15, machine.Pin.IN)

def keyboard_test():
    k = keyboard.Keyboard()

    # press and release
    k.press(k.MOD_LEFT_GUI, k.MOD_LEFT_SHIFT, 0x10) # CMD+SHIFT+M
    #k.press(0x10) #m
    #k.release(0x10)
    k.release(k.MOD_LEFT_GUI, k.MOD_LEFT_SHIFT, 0x10) # CMD+SHIFT+M
    print("CMD+SHIFT+M")
    
def keyboard_testLetter():
    k = keyboard.Keyboard()
    k.press(0x10) #M
    k.release(0x10)
    k.release_all()

while True:
    value_button = button.value()
    print(value_button)
    if value_button == 1:
        keyboard_test()
        
    utime.sleep(.5)
    #keyboard_testLetter()


#This is a testcomment