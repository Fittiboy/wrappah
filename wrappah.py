#!/home/fitti/projects/wrappah/venv/bin/python
import pyperclip
from pyautogui import keyDown, keyUp, press
from time import sleep


while True:
    to_wrap = pyperclip.waitForNewPaste()
    pyperclip.copy("What's \"" + to_wrap.strip("\n").strip() + "\"?")
    keyDown("control")
    press("v")
    keyUp("control")
    sleep(.1)
    press("enter")
    print("Copied!")
