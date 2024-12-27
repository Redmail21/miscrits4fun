import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con


if __name__ == "__main__":
   
    currMx,currMy = pyautogui.position()

    print(currMx,currMy)