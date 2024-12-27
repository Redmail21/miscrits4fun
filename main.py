import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con

TIME_FACTOR_DIV = 1

GAMESTATES = ["outside", "inbattle", "afterbattle", "train"]
GAMESTATE = GAMESTATES[0]

entranceToTown = (213,507)
entranceToForest = (700,280) #not accurate yet

def print_gamestate():
   global GAMESTATE   
   print(f'Game state: {GAMESTATE}')

def check_gamestate():
   global GAMESTATE

   if(pyautogui.locateOnScreen("assets/png/ui01.png", confidence=0.65) is not None):
      GAMESTATE = GAMESTATES[0]
      print_gamestate()
      
   elif (pyautogui.locateOnScreen("assets/png/ui00.png", confidence=0.5) is not None):
      GAMESTATE = GAMESTATES[1]
      print_gamestate()

   else:
      print_gamestate()
  
  

def find_bush():

    if(GAMESTATE==GAMESTATES[0]):
        loc = pyautogui.locateCenterOnScreen("assets/png/element00.png", confidence=0.7)
        pyautogui.moveTo(loc)
        pyautogui.click()
        time.sleep(1)

def battle():
   if(GAMESTATE==GAMESTATES[1]):
      loc = pyautogui.locateCenterOnScreen("assets/png/ui00.png", confidence=0.55)
      pyautogui.moveTo(loc)
      pyautogui.click()
      time.sleep(1)

    

if __name__ == "__main__":
   time.sleep(1.5)
   
   while 1:

    if(keyboard.is_pressed('q')):
        break
    

    check_gamestate()
    find_bush()
    battle()

    currMx,currMy = pyautogui.position()
    print(currMx,currMy)

    print(GAMESTATE)