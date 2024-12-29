import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con

TIME_FACTOR_DIV = 1

CAN_TRAIN = False

TRAIN_WITH_PLATINUM = True
ELEMENT_INDEX = 0
ELEMENTS_ARRAY_ACTUAL =  ["element00.png","element01.png"]
GAMESTATES = ["outside", "inbattle", "afterbattle", "training"]
GAMESTATE = GAMESTATES[0]

#entranceToTown = (213,507)
#entranceToForest = (700,280) #not accurate yet, UPDATE: NOT NEEDED, ELEMENTS COOLDOWN

def print_gamestate():
   global GAMESTATE   
   print(f'Game state: {GAMESTATE}')

def check_gamestate():
    global GAMESTATE   
    

    try:
        if (pyautogui.locateOnScreen("assets/png/ui01.png", confidence=0.7) is not None):
            GAMESTATE = GAMESTATES[0]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass

    try:
        if (pyautogui.locateOnScreen("assets/png/ui00.png", confidence=0.7) is not None):
            GAMESTATE = GAMESTATES[1]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass

    try:
        if (pyautogui.locateOnScreen("assets/png/ui02.png", confidence=0.7) is not None):
            GAMESTATE = GAMESTATES[2]
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass


    try: 
        pass
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
              time.sleep(1.5)

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
    global CAN_TRAIN, GAMESTATE

     

    if(CAN_TRAIN):

        GAMESTATE = GAMESTATES[3]

        try:

          loc = pyautogui.locateCenterOnScreen("assets/png/ui11.png", confidence=0.6)
          pyautogui.moveTo(loc)
          pyautogui.click()
          time.sleep(2)

        except pyautogui.ImageNotFoundException:
            pass

    #?locate all the trainable miscrits        


        try: 
            print("starting locateAllOnScreen")
            trainable_miscrits_locs = (pyautogui.locateAllOnScreen("assets/png/ui05a.png", confidence=0.6))
            

            for loct in trainable_miscrits_locs:

                print("training miscrit")
                center = pyautogui.center(loct)

                pyautogui.click(center)
                time.sleep(1)
                
                
                
                loc = pyautogui.locateCenterOnScreen("assets/png/ui07.png", confidence=0.6)
                pyautogui.moveTo(loc)
                pyautogui.click()
                time.sleep(1)          


                if(TRAIN_WITH_PLATINUM):
                    loc = pyautogui.locateCenterOnScreen("assets/png/ui08.png", confidence=0.6)
                    pyautogui.moveTo(loc)
                    pyautogui.click()
                    time.sleep(1)          
              
                    
                loc = pyautogui.locateCenterOnScreen("assets/png/ui09.png", confidence=0.6)
                pyautogui.moveTo(loc)
                pyautogui.click()
                time.sleep(1)   
           
        except pyautogui.ImageNotFoundException:
            pass
       
    
    #?exit

    try:

        loc = pyautogui.locateCenterOnScreen("assets/png/ui10.png", confidence=0.5)
        CAN_TRAIN = False
        pyautogui.moveTo(loc)
        pyautogui.click()
        time.sleep(0.5)    

    except pyautogui.ImageNotFoundException:
        pass

    

if __name__ == "__main__":
   time.sleep(1.5)
   
   while 1:

    if(keyboard.is_pressed('x')):
        time.sleep(0.1)
        break
    

    check_gamestate()
    time.sleep(0.1)
    find_element()
    time.sleep(0.1)
    battle()
    time.sleep(0.1)
    after_battle()
    time.sleep(0.1)
    train_miscrit()
    time.sleep(0.1)


    # currMx,currMy = pyautogui.position()
    # print(currMx,currMy)
    #print(GAMESTATE)
    #print(ELEMENTS_ARRAY_ACTUAL)

    time.sleep(0.2)