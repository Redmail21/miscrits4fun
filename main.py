import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con

TIME_FACTOR_DIV = 1

CAN_TRAIN = False

ELEMENT_INDEX = 0
ELEMENTS_ARRAY_ACTUAL =  ["element00.png","element01.png"]
GAMESTATES = ["outside", "inbattle", "afterbattle"]
GAMESTATE = GAMESTATES[0]

#entranceToTown = (213,507)
#entranceToForest = (700,280) #not accurate yet, UPDATE: NOT NEEDED, ELEMENTS COOLDOWN



    
    

def print_gamestate():
   global GAMESTATE   
   print(f'Game state: {GAMESTATE}')

def check_gamestate():
    global GAMESTATE   
    #pyautogui.useImageNotFoundException()  outdated

    try:
        if (pyautogui.locateOnScreen("assets/png/ui01.png", confidence=0.5) is not None):
            GAMESTATE = GAMESTATES[0]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass

    try:
        if (pyautogui.locateOnScreen("assets/png/ui00.png", confidence=0.5) is not None):
            GAMESTATE = GAMESTATES[1]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass

    try:
        if (pyautogui.locateOnScreen("assets/png/ui02.png", confidence=0.5) is not None):
            GAMESTATE = GAMESTATES[2]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass
     

def find_element():
    global GAMESTATE,ELEMENT_INDEX

    time.sleep(0.5)
    print(f"Current GAMESTATE: {GAMESTATE}")
    print(f"Current ELEMENT_INDEX: {ELEMENT_INDEX}")


    if(GAMESTATE==GAMESTATES[0]):
        try:
            
            loc = pyautogui.locateCenterOnScreen( "assets/png/"+ELEMENTS_ARRAY_ACTUAL[ELEMENT_INDEX], confidence=0.6)
            pyautogui.moveTo(loc)
            pyautogui.click()
            print(ELEMENT_INDEX)
            ELEMENT_INDEX = 1 if ELEMENT_INDEX == 0 else 0
            time.sleep(2.5)
            GAMESTATE = GAMESTATES[1]

        except pyautogui.ImageNotFoundException:
            pass
                

def battle():
   if(GAMESTATE==GAMESTATES[1]):          
      try:
          loc = pyautogui.locateCenterOnScreen("assets/png/ui00.png", confidence=0.45)
          pyautogui.moveTo(loc)
          pyautogui.click()
          time.sleep(1)

      except pyautogui.ImageNotFoundException:
        pass


def after_battle():
    global CAN_TRAIN,GAMESTATE

    if(GAMESTATE==GAMESTATES[2]):            
      try:
          
          try:                            
              if(pyautogui.locateCenterOnScreen("assets/png/ui05.png", confidence=0.5)):
                                                      
                  CAN_TRAIN = True
                  print("Can Train now.")

          except pyautogui.ImageNotFoundException:
              pass
          
          loc = pyautogui.locateCenterOnScreen("assets/png/ui03.png")

          
          
          pyautogui.moveTo(loc)
          pyautogui.click()
          #print("did something")
          
          time.sleep(1)
          GAMESTATE=GAMESTATES[0]
          


      except pyautogui.ImageNotFoundException:
        pass

def train_miscrit():

    pass
      
    

if __name__ == "__main__":
   time.sleep(1.5)
   
   while 1:

    if(keyboard.is_pressed('q')):
        break
    

    check_gamestate()
    find_element()
    battle()
    after_battle()


    #currMx,currMy = pyautogui.position()
    #print(currMx,currMy)
    #print(GAMESTATE)
    #print(ELEMENTS_ARRAY_ACTUAL)

    time.sleep(0.1)