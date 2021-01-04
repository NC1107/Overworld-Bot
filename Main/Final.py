# # Final Version Goal:
# # Avoid image recognition for finding buttons
# #     less automatated, more efficient
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
#                     -Potion of choicesss
#     ---Return To beginning of farming function
import glob
import random
from datetime import datetime

import pyautogui as PAG
import win32gui as Win
import cv2 as C
import time

StartTime = datetime.now()
print("Program has started running at: " + str(StartTime))

CBL = (476, 606)  # Continue Button Location
ABL = (372, 892)  # Attack Button Location
VBL = (484, 980)  # Victory Button Location
HBL = (582, 999)  # Heal Button Location
PBL = (578, 818)  # Potion Button Location
XBL = (480, 1030)  # 'X' Button Location
SBL = (480, 825)  # Location necessary for scroll
EXP = (480, 500)  # EXP Potion
LCL = (314, 640)  # Lucky Coin
OCL = (560, 650)  # Occult Candle
TL = (638, 644)  # Torch


def CreateMonsterList(MonsterDirectory):
    SML = []
    path = glob.glob(MonsterDirectory)
    for img in path:
        SML.append(img)
    return SML


def GetScreenshot(Selected_Window):
    if Selected_Window:
        window = Win.FindWindow(None, Selected_Window)
        if window:
            Win.SetForegroundWindow(window)
            x, y, x1, y1 = Win.GetClientRect(window)
            x, y = Win.ClientToScreen(window, (x + 240, y + 240))
            x1, y1 = Win.ClientToScreen(window, ((x1 - 240) - x, (y1 - 240) - y))
            Screenshot = PAG.screenshot("CurrentScreenshot.png", region=(x, y, x1, y1))
            print("updated 'CurrentScreenshot.png'")
            return Screenshot
    else:
        print("invalid Source")
        return None


def FoundMonster(Monster):
    print("Looking for " + Monster)
    GetScreenshot('Pixel 5')
    MI = C.imread('CurrentScreenshot.png')
    GMI = C.cvtColor(MI, C.COLOR_BGR2GRAY)
    S = C.imread(Monster, 0)
    width, height = S.shape[:2]
    MatchChecker = C.matchTemplate(GMI, S, C.TM_CCOEFF_NORMED)
    accuracy = .9
    min_val, max_val, min_loc, max_loc = C.minMaxLoc(MatchChecker)
    if max_val > accuracy:
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        CenterCords = [0, 1]
        CenterCords[0] = ((top_left[0] + bottom_right[0]) / 2) + 238
        CenterCords[1] = ((top_left[1] + bottom_right[1]) / 2) + 245
        C.rectangle(MI, top_left, bottom_right, 255, 2)
        C.rectangle(MI, CenterCords, CenterCords, 255, 5)

        if len(CenterCords) != 0:
            print(Monster + " Was Found!")
            PAG.moveTo(CenterCords[0] + width, CenterCords[1] + height, duration=.2)
            Fx, Fy = PAG.position()
            PAG.click(Fx + random.uniform(0, 1.0), Fy + random.uniform(0, 1), duration=.2)
            C.imwrite("detected.png", MI)
            return True
        else:
            return False


while True:

    CurrentTime = datetime.now()
    for Monsters in CreateMonsterList(r"C:\Users\18862\Desktop\Overworld Bot\Main\ScaledMonsters\*.png"):
        if FoundMonster(Monsters):
            # Hit Continue Button
            PAG.moveTo(CBL[0], CBL[1], duration=.6)
            PAG.click(CBL[0] + random.uniform(1.0, 10.0), CBL[1] + random.uniform(.01, 1), duration=.1)
            print("Clicked Continue")
            # Hit Attack Button
            PAG.click(ABL[0] + random.uniform(10, 30), ABL[1] + random.uniform(1.0, 5.0), duration=.8)
            print("Clicked Attack 1")
            # Hit Attack Button
            PAG.click(ABL[0] + random.uniform(3.0, 10.0), ABL[1] + random.uniform(1.0, 5.0), duration=4)
            print("Clicked Attack 2")
            # Hit Victory Button
            PAG.click(VBL[0] + random.uniform(1.0, 20), VBL[1] - 15, duration=3)
            print("Clicked Continue")
            # Hit Heal Button
            PAG.click(HBL[0] + random.uniform(1.0, 8.0), HBL[1] + random.uniform(1.0, 8.0), duration=.8)
            print("Clicked Heal Menu")
            # Hit Mana Button
            PAG.click(PBL[0] + random.uniform(1.0, 5.0), PBL[1] + random.uniform(1.0, 5.0), duration=1)
            print("Clicked Potion")
            # Hit 'x' Button
            PAG.click(XBL[0] + random.uniform(1.0, 5.0), XBL[1] + random.uniform(1.0, 5.0), duration=1)
            print("Clicked X")
            time.sleep(2)


        def XPBuff():
            print("Timer went off")
            PAG.click(HBL[0] + random.uniform(1.0, 5.0), HBL[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.moveTo(SBL[0] + random.uniform(1.0, 5.0), SBL[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.vscroll(-800)

            print("Done scroll?")
            PAG.click(EXP[0] + random.uniform(1.0, 5.0), EXP[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.click(LCL[0] + random.uniform(1.0, 5.0), LCL[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.click(OCL[0] + random.uniform(1.0, 5.0), OCL[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.click(TL[0] + random.uniform(1.0, 5.0), TL[1] + random.uniform(1.0, 5.0), duration=1)
            PAG.click(XBL[0] + random.uniform(1.0, 5.0), XBL[1] + random.uniform(1.0, 5.0), duration=1)


        if CurrentTime.hour == StartTime.hour + 1:
            print("HOUR SAME")
            if CurrentTime.minute == StartTime.minute:
                print("-----------------------REBUFFING-----------------")
                XPBuff()
                StartTime = datetime.now()
