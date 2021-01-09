# # Final Version Goal:
# # Avoid image recognition for finding buttons
# #     less automated, more efficient
# # Require:
# #   -Continue Screen(Fight Monster)
# #   -Attack Screen
# #   -Victory/Defeat Continue Screen
# #   -Potion Screen
# #
# # Layout
#     -Setup Button Locations
#         +Provide Scene Screenshots
#         +Have User attack a monster & Save Locations
#     -Begin Farming
#         +Take Screenshot of Main Scene
#             +When monster found
#                 +Run Continue button function
#                 +Run attack script
#                     -Requires check to ensure player or monster is dead
#                         -image rec of either att button or continue(victory) button
#                 +Click Victory/Defeat button to return to main scene
#                 +Click Heal Button
#                     -Potion of choices
#     ---Return To beginning of farming function
import glob
import random
from datetime import datetime

import pyautogui as pag
import win32gui as win
import cv2 as c
import time

StartTime = datetime.now()
print("Program has started running at: " + str(StartTime))

CBL = (476, 606)  # Continue Button Location
ABL = (372, 892)  # Attack Button Location
VBL = (484, 980)  # Victory Button Location
HBL = (582, 999)  # Heal Button Location
PBL = (578, 750)  # Potion Button Location
XBL = (480, 1030)  # 'X' Button Location
SBL = (480, 825)  # Location necessary for scroll
EXP = (480, 500)  # EXP Potion
LCL = (314, 640)  # Lucky Coin
OCL = (560, 650)  # Occult Candle
TL = (638, 644)  # Torch


def create_monster_list(monster_directory):
    sml = []
    path = glob.glob(monster_directory)
    for img in path:
        sml.append(img)
    return sml


def get_screenshot(selected_window):
    if selected_window:
        window = win.FindWindow(None, selected_window)
        if window:
            win.SetForegroundWindow(window)
            x, y, x1, y1 = win.GetClientRect(window)
            x, y = win.ClientToScreen(window, (x + 240, y + 240))
            x1, y1 = win.ClientToScreen(window, ((x1 - 240) - x, (y1 - 240) - y))
            screenshot = pag.screenshot("CurrentScreenshot.png", region=(x, y, x1, y1))
            print("updated 'CurrentScreenshot.png'")
            return screenshot
    else:
        print("invalid Source")
        return None


def found_monster(_monster):
    print("Looking for " + _monster)
    get_screenshot('SM-G973U')
    mi = c.imread('CurrentScreenshot.png')
    gmi = c.cvtColor(mi, c.COLOR_BGR2GRAY)
    s = c.imread(_monster, 0)
    width, height = s.shape[:2]
    match_checker = c.matchTemplate(gmi, s, c.TM_CCOEFF_NORMED)
    accuracy = .8
    min_val, max_val, min_loc, max_loc = c.minMaxLoc(match_checker)
    if max_val > accuracy:
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        center_cords = [0, 1]
        center_cords[0] = ((top_left[0] + bottom_right[0]) / 2) + 238
        center_cords[1] = ((top_left[1] + bottom_right[1]) / 2) + 245
        c.rectangle(mi, top_left, bottom_right, 255, 2)
        c.rectangle(mi, center_cords, center_cords, 255, 5)

        if len(center_cords) != 0:
            print(_monster + " Was Found!")
            pag.moveTo(center_cords[0] + width, center_cords[1] + height, duration=.2)
            fx, fy = pag.position()
            pag.click(fx + random.uniform(0, 1.0), fy + random.uniform(0, 1), duration=.2)
            c.imwrite("detected.png", mi)
            return True
        else:
            return False


while True:
    CurrentTime = datetime.now()
    for Monsters in create_monster_list(r"C:\Users\Nick Conn\Documents\GitHub\Overworld-Bot\Main\ScaledMonsters\*.png"):
        if found_monster(Monsters):
            # Hit Continue Button
            pag.moveTo(CBL[0], CBL[1], duration=.6)
            pag.click(CBL[0] + random.uniform(1.0, 10.0), CBL[1] + random.uniform(.01, 1), duration=.1)
            print("Clicked Continue")
            # Hit Attack Button
            pag.click(ABL[0] + random.uniform(10, 30), ABL[1] + random.uniform(1.0, 5.0), duration=.8)
            print("Clicked Attack 1")
            # Hit Attack Button
            pag.click(ABL[0] + random.uniform(3.0, 10.0), ABL[1] + random.uniform(1.0, 5.0), duration=4)
            print("Clicked Attack 2")
            # Hit Victory Button
            pag.click(VBL[0] + random.uniform(1.0, 20), VBL[1] - 15, duration=3)
            print("Clicked Continue")
            # Hit Heal Button
            pag.click(HBL[0] + random.uniform(1.0, 8.0), HBL[1] + random.uniform(1.0, 8.0), duration=.8)
            print("Clicked Heal Menu")
            # Hit Mana Button
            pag.click(PBL[0] + random.uniform(1.0, 5.0), PBL[1] + random.uniform(1.0, 1.3), duration=1.2)
            print("Clicked Potion")
            # Hit 'x' Button
            pag.click(XBL[0] + random.uniform(1.0, 5.0), XBL[1] + random.uniform(1.0, 5.0), duration=1)
            print("Clicked X")
            time.sleep(2)


        def xp_buff():
            print("Timer went off")
            pag.click(HBL[0] + random.uniform(1.0, 5.0), HBL[1] + random.uniform(1.0, 5.0), duration=1)
            pag.moveTo(SBL[0] + random.uniform(1.0, 5.0), SBL[1] + random.uniform(1.0, 5.0), duration=1)
            pag.vscroll(-800)

            print("Done scroll?")
            pag.click(EXP[0] + random.uniform(1.0, 5.0), EXP[1] + random.uniform(1.0, 5.0), duration=1)
            pag.click(LCL[0] + random.uniform(1.0, 5.0), LCL[1] + random.uniform(1.0, 5.0), duration=1)
            pag.click(OCL[0] + random.uniform(1.0, 5.0), OCL[1] + random.uniform(1.0, 5.0), duration=1)
            pag.click(TL[0] + random.uniform(1.0, 5.0), TL[1] + random.uniform(1.0, 5.0), duration=1)
            pag.click(XBL[0] + random.uniform(1.0, 5.0), XBL[1] + random.uniform(1.0, 5.0), duration=1)


        if CurrentTime.hour == StartTime.hour + 1:
            print("HOUR SAME")
            if CurrentTime.minute == StartTime.minute:
                print("-----------------------REBUFFING-----------------")
                xp_buff()
                StartTime = datetime.now()
