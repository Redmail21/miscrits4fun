import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con
import pygetwindow as gw

#! USE THE WORD "@NOTE@"

window_title = "Miscrits (DEBUG)"
window = gw.getWindowsWithTitle(window_title)[0]  # Get the first match

CAN_TRAIN = False
NEED_HEAL = False
TRAIN_WITH_PLATINUM = False
ELEMENT_INDEX = 0

ELEMENTS_ARRAY_ACTUAL =  ["element00.png","element01.png"]
FILLER_PROMPTS = ["ui03.png","ui06a.png", "ui09.png", "ui15.png", "ui17.png"]
GAMESTATES = ["outside", "inbattle", "afterbattle", "training"]
GAMESTATE = GAMESTATES[0]

#entranceToTown = (213,507)
#entranceToForest = (700,280) #not accurate yet, UPDATE: NOT NEEDED, ELEMENTS COOLDOWN

def click_images_until_none(images, confidence=0.7, delay=1):

    if window:
        x, y, width, height = window.left, window.top, window.width, window.height

        # Step 2: Define a region (e.g., with margins)
        margin = 10  # Adjust the margin as needed
        region = (x + margin, y + margin+200, width - 2 * margin, height - 2 * margin)
        print("Checking for extra prompts/stuff")
        
        try:
            while True:
                found_any = False

                for image in images:
                    try:
                        
                        locations = list(pyautogui.locateAllOnScreen("assets/png/" + image,region=region, confidence=confidence))

                        if locations:
                            found_any = True
                            print(f"\n Found {len(locations)} instances of {image}")

                            
                            for loc in locations:
                                center = pyautogui.center(loc)
                                pyautogui.moveTo(center)
                                pyautogui.click()
                                time.sleep(delay)

                    except pyautogui.ImageNotFoundException:
                        # 
                        print(f"\n Image {image} not found. \n")
                        continue

                    except Exception as e:
                        
                        #print(f"Unexpected error with image {image}: {e}")
                        continue

                if not found_any:
                    #print("No images found. Ending.")
                    break
        except KeyboardInterrupt:
            print("Interrupted by user. Exiting.")

        

def print_gamestate():
   global GAMESTATE   
   print(f'Game state: {GAMESTATE}')

def check_gamestate():
    global GAMESTATE,ELEMENT_INDEX
    

    try:
        if (pyautogui.locateOnScreen("assets/png/ui01.png", confidence=0.7) is not None):
            GAMESTATE = GAMESTATES[0]
            ELEMENT_INDEX = 1 if ELEMENT_INDEX == 0 else 0
            #print_gamestate()

    except pyautogui.ImageNotFoundException:
        pass

    try:
        if (pyautogui.locateOnScreen("assets/png/ui13.png", confidence=0.65) is not None):
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


    
     

def find_element():
    global GAMESTATE,ELEMENT_INDEX


    if(GAMESTATE==GAMESTATES[0]):
        try:
            
            loc = pyautogui.locateCenterOnScreen( "assets/png/"+ELEMENTS_ARRAY_ACTUAL[ELEMENT_INDEX], confidence=0.6)
             
            pyautogui.moveTo(loc)
            pyautogui.click()
            print(ELEMENT_INDEX)
            ELEMENT_INDEX = 1 if ELEMENT_INDEX == 0 else 0
            time.sleep(2)
            GAMESTATE = GAMESTATES[1]

        except pyautogui.ImageNotFoundException:
            pass
                

def battle():
   
   if(GAMESTATE==GAMESTATES[1]):          
      try:
          
        
          loc = pyautogui.locateCenterOnScreen("assets/png/ui00.png", confidence=0.8)

          if(loc is None):

            try: 
                pyautogui.moveTo(pyautogui.locateCenterOnScreen("assets/png/ui14.png", confidence=0.7,grayscale=True))
                pyautogui.click()
                print("Clicking arrow until finding attack")  
                loc = pyautogui.locateCenterOnScreen("assets/png/ui00.png", confidence=0.8)
                time.sleep(0.3)

            except pyautogui.ImageNotFoundException:
                print("Couldn't click attacks arrow.")


          pyautogui.moveTo(loc)
          pyautogui.click()
          time.sleep(1)

      except pyautogui.ImageNotFoundException:
        pass


def after_battle():
    global CAN_TRAIN,GAMESTATE,NEED_HEAL

    if(GAMESTATE==GAMESTATES[2]):            
      try:
          
          try:                            
              time.sleep(5)

              if(pyautogui.locateCenterOnScreen("assets/png/ui05.png", confidence=0.5)):
                                                      
                  CAN_TRAIN = True
                  print("Can Train now.")

                         


                  

          except pyautogui.ImageNotFoundException:
              pass
                 
          try:                     
                print("Checking miscrits health.")
                fallen_crits = list(pyautogui.locateAllOnScreen("assets/png/ui16.png", confidence=0.9))
                
                print(f'#downed(Including enemy) {len(fallen_crits)}')

                if(len(fallen_crits) > 2):
                    NEED_HEAL = True
                    print("Need a medic")


          except pyautogui.ImageNotFoundException:                    
                print("No need to heal miscrits")

          loc = pyautogui.locateCenterOnScreen("assets/png/ui03.png")
          pyautogui.moveTo(loc)
          pyautogui.click()
          #print("did something")    
          time.sleep(1)                
          GAMESTATE=GAMESTATES[0]
          time.sleep(1)
           
          


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
            trainable_miscrits_locs = (pyautogui.locateAllOnScreen("assets/png/ui05a.png", confidence=0.9))
            
            #^ TEST            

            for loct in trainable_miscrits_locs:

                print("training miscrit")
                center = pyautogui.center(loct)

                pyautogui.click(center)
                time.sleep(1)
                
                
                #* CHECK FOR EVOLUTIONS

                loc = pyautogui.locateCenterOnScreen("assets/png/ui07.png", confidence=0.7)
                pyautogui.moveTo(loc)
                pyautogui.click()
                time.sleep(1)          


                if(TRAIN_WITH_PLATINUM):
                    loc = pyautogui.locateCenterOnScreen("assets/png/ui08.png", confidence=0.8)
                    pyautogui.moveTo(loc)
                    pyautogui.click()
                    time.sleep(1)                                        
                    
                loc = pyautogui.locateCenterOnScreen("assets/png/ui09.png", confidence=0.8)
                pyautogui.moveTo(loc)
                pyautogui.click()
                time.sleep(1)   

                click_images_until_none(FILLER_PROMPTS)
           
        except pyautogui.ImageNotFoundException:
            pass
       
    
    #?exit

    try:

        loc = pyautogui.locateCenterOnScreen("assets/png/ui10.png", confidence=0.8)
        CAN_TRAIN = False
        pyautogui.moveTo(loc)
        pyautogui.click()
        time.sleep(0.5)    

    except pyautogui.ImageNotFoundException:
        pass

def heal_miscrits():
    global NEED_HEAL

    if(NEED_HEAL == True):
        if(GAMESTATE==GAMESTATES[0]):

            try:             
                loc = pyautogui.locateCenterOnScreen("assets/png/ui04.png", confidence=0.65)

                pyautogui.moveTo(loc)
                pyautogui.click()                        
                print("Healing now")
                NEED_HEAL = False
                time.sleep(0.3)

            except pyautogui.ImageNotFoundException:
                pass

        
    

if __name__ == "__main__":
      
   while 1:

    if(keyboard.is_pressed('x')):
        time.sleep(0.1)
        break
    

    print(f"Current GAMESTATE: {GAMESTATE}")
    #print(f"Current ELEMENT_INDEX: {ELEMENT_INDEX}")

    check_gamestate()
    

    find_element()    
    

    battle()
    
     

    after_battle()
   

    train_miscrit()
    
    heal_miscrits()

    if(GAMESTATE==GAMESTATES[0]):
        click_images_until_none(FILLER_PROMPTS)
    
 
    # currMx,currMy = pyautogui.position()
    # print(currMx,currMy)


    time.sleep(0.2)