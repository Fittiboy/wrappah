#!/home/fitti/projects/wrappah/venv/bin/python
import pyperclip
from pyautogui import hotkey, press
from time import sleep


while True:
    to_wrap = pyperclip.waitForNewPaste()
    pyperclip.copy("What's \"" + to_wrap.strip("\n").strip() + "\"?")
    hotkey("ctrl", "v")
    sleep(.2)
    press("enter")
    print("Copied!")
