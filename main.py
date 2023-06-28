from directKeys import *
from ScreenDetector import *
import time
import random
import pyscreenshot
from pynput.keyboard import Key, Controller

def screenshot():
    keyboard = Controller()
    image = pyscreenshot.grab()
    num = str(1)
    image.save(f"screenshots\\Intermarche_{num}.png")
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    print('done')
    time.sleep(2)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print('done')
    time.sleep(2)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print('done')
    time.sleep(2)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print('done')
    time.sleep(2)
    keyboard.press(Key.up)
    keyboard.release(Key.up)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screenshot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
