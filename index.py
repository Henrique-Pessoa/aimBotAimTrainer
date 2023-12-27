import pyautogui
import keyboard
from click import click


while keyboard.is_pressed("q") == False:
    img = pyautogui.screenshot(region=(480, 350, 880, 500))
    for x in range(0, 880, 4):
        for y in range(0, 500, 4):
            r, g, b = img.getpixel((x, y))
            if r == 255:
                click(x + 480, y + 350)
                print(x)
                break
