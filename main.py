import pyautogui as gui
import time
import random, string


number = input('Enter number ')

time.sleep(5)

for i in range(int(number)):
    stri = string.ascii_lowercase
    message = "".join(random.sample(stri, 230))
    gui.typewrite(message)
    gui.press("Enter")

