import glob

from PIL import Image
import cv2
import numpy
import pyautogui
import win32gui


def GetMonsterScreenshot(Selected_Window):
    if Selected_Window:
        window = win32gui.FindWindow(None, Selected_Window)
        if window:
            win32gui.SetForegroundWindow(window)
            x, y, x1, y1 = win32gui.GetClientRect(window)
            x, y = win32gui.ClientToScreen(window, (x, y + 130))
            x1, y1 = win32gui.ClientToScreen(window, (x1 - x, (y1 - 140) - y))
            Screenshot = pyautogui.screenshot("CurrentScreenshot.png", region=(x, y, x1, y1))
            print("updated 'CurrentScreenshot.png'")
            return Screenshot
    else:
        print("invalid Source")
        return None


def MonsterMatches(S):
    print("Looking for matches that match: " + S)
    MI = cv2.imread('CurrentScreenshot.png')
    GMI = cv2.cvtColor(MI, cv2.COLOR_BGR2GRAY)
    Search = cv2.imread(S, 0)
    width, height = Search.shape[:2]
    MatchChecker = cv2.matchTemplate(GMI, Search, cv2.TM_CCOEFF_NORMED)
    accuracy = .65
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(MatchChecker)
    if max_val > accuracy:
        top_left = max_loc
        bottom_right = (top_left[0] + width, top_left[1] + height)
        CenterCords = [0, 1]
        CenterCords[0] = (top_left[0] + bottom_right[0]) / 2
        CenterCords[1] = (top_left[1] + bottom_right[1]) / 2

        cv2.rectangle(MI, top_left, bottom_right, 255, 2)
        cv2.imwrite("detected.png", MI)
        if len(CenterCords) != 0:
            print(" Match Located At X:" + str(CenterCords[0] + width) + " Y: " + str(CenterCords[1] + height))
            return True
        else:
            return False
    print("Could not find: " + S + "--------------------------------------ERROR----------------")


def SearchForMonster(MonsterList):
    image = Image.open('CurrentScreenshot.png')
    opencvImage = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)

    for monsters in MonsterList:
        if MonsterMatches(monsters):
            cv2.imwrite("detected.png", opencvImage)


def CreateMonsterList(MonsterDirectory):
    SML = []
    path = glob.glob(MonsterDirectory)
    for img in path:
        SML.append(img)
    return SML


GetMonsterScreenshot('Pixel 5')
SearchForMonster(CreateMonsterList(r"C:\Users\18862\Desktop\Overworld Bot\Main\ScaledMonsters\*.png"))
