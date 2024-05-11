from PIL import ImageTk, Image
import tkinter as tk
from threading import Thread
import pyautogui


def run():
    img = pyautogui.screenshot()
    color = img.getpixel(pyautogui.position())
    print("#{0:02x}{1:02x}{2:02x}".format(*color))


if __name__ == "__main__":
    run()
