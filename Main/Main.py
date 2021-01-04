import time
import sys
import time

import pyautogui
import win32gui
import glob
import cv2
import random

Farming = True
time_start = time.time()
seconds = 0
minutes = 0





# Detects if monster is found
def IfMatches(S):
    print("Looking for matches that match: " + S)
    GetScreenshot('Pixel 5')
    MI = cv2.imread('CurrentScreenshot.png')
    GMI = cv2.cvtColor(MI, cv2.COLOR_BGR2GRAY)
    Search = cv2.imread(S, 0)
    width, height = Search.shape[:2]
    MatchChecker = cv2.matchTemplate(GMI, Search, cv2.TM_CCOEFF_NORMED)
    accuracy = .5
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(MatchChecker)
    if max_val > accuracy:
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        CenterCords = [0, 1]
        CenterCords[0] = (top_left[0] + bottom_right[0]) / 2
        CenterCords[1] = (top_left[1] + bottom_right[1]) / 2

        cv2.rectangle(MI, top_left, bottom_right, 255, 2)
        if len(CenterCords) != 0:
            print(" Match Located At X:" + str(CenterCords[0] + width) + " Y: " + str(CenterCords[1] + height))

            pyautogui.moveTo(CenterCords[0] + width, CenterCords[1] + height, duration=.1)
            cv2.imwrite("detected.png", MI)
            time.sleep(1.5)

            return True
        else:
            return False
    print("Could not find: " + S + "--------------------------------------ERROR----------------") 


# Gets screenshot of game
def GetScreenshot(Selected_Window):
    if Selected_Window:
        window = win32gui.FindWindow(None, Selected_Window)
        if window:
            win32gui.SetForegroundWindow(window)
            x, y, x1, y1 = win32gui.GetClientRect(window)
            x, y = win32gui.ClientToScreen(window, (x, y))
            x1, y1 = win32gui.ClientToScreen(window, (x1 - x, y1 - y))
            Screenshot = pyautogui.screenshot("CurrentScreenshot.png", region=(x, y, x1, y1))
            print("updated 'CurrentScreenshot.png'")
            return Screenshot
    else:
        print("invalid Source")
        return None


# Creates list of attack-able monsters
def CreateMonsterList(MonsterDirectory):
    SML = []
    path = glob.glob(MonsterDirectory)
    for img in path:
        SML.append(img)
    return SML


# Heals Player, Mana only to buff 'realmshifter' world bonus
def HealScript():
    path = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\Heal_Button_Scaled.PNG'
    potion = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\ManaPotion_Scaled.PNG'
    Close = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\X_Button_Scaled.PNG'
    if IfMatches(path):
        x, y = pyautogui.position()
        pyautogui.leftClick(x - random.uniform(5.0, 10), y + random.uniform(1.0, 2.0), duration=.2)
        while not IfMatches(potion):
            IfMatches(potion)
        x, y = pyautogui.position()
        pyautogui.click(x + random.uniform(1.0, 5.0), y + random.uniform(1.0, 5.0), duration=.2)
        if IfMatches(Close):
            x, y = pyautogui.position()
            pyautogui.click(x + random.uniform(1.0, 5.0), y + random.uniform(1.0, 5.0), duration=.1)


# Attacks the monster undead the player or monster is dead. runs HealScript() after
def AttackScript():
    try:
        path = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\Basic_Scaled_Attack.PNG'
        Continue = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\Continue_Logo_Scaled.PNG'
        Attack = True

        while Attack:
            while not IfMatches(path):
                IfMatches(path)
            x, y = pyautogui.position()
            pyautogui.click(x + random.uniform(3.0, 20), y + random.uniform(3.0, 10), duration=.2)
            if IfMatches(Continue):
                pyautogui.moveTo(260 + random.uniform(1.0, 5.0), 950 + random.uniform(1.0, 5.0), duration=.1)
                x, y = pyautogui.position()
                pyautogui.click(x + random.uniform(3.0, 20), y + random.uniform(3.0, 10), duration=.1)
                time.sleep(.5) 
                Attack = False
        time.sleep(1)
        HealScript()
    except KeyboardInterrupt:
        Attack = False
        print("Looping Stopped!")


# Click the continue button after finding the monster, if successful, runs AttackScript()
def AttackMonster():
    try:
        path = r'C:\Users\18862\Desktop\Overworld Bot\Main\ScaledGUIs\Green_Battle_Logo_Scaled.PNG'
        while not IfMatches(path):
            IfMatches(path)
        pyautogui.leftClick(duration=.1)
        AttackScript()
    except KeyboardInterrupt:
        print("Looping Stopped!")


# Search for monsters on screen, if found runs AttackMonster()
def SearchForMonster(MonsterList):
    for monsters in MonsterList:
        if MonsterMatches(monsters):
            time.sleep(1)
            pyautogui.click(duration=.2)
            time.sleep(1)
            AttackMonster()


# Set Farming to True to begin
while Farming:
    SearchForMonster(CreateMonsterList(r"C:\Users\18862\Desktop\Overworld Bot\Main\ScaledMonsters\*.png"))
