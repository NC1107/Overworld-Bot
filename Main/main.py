import glob
import random
from datetime import datetime

import pyautogui as pag
import win32gui as win
import cv2 as c
import Scripts.Buttons
import Scripts.Rebuff
import Scripts.Colors
import os
import keyboard


class CurrentSetup:

    def __init__(self, device='Test', farming='False', autobuff='False'):
        self._Device = device
        self._Farming = farming
        self._AutoBuff = autobuff

    def get_device(self):
        return self._Device

    def get_farming(self):
        return self._Farming

    def get_autobuff(self):
        return self._AutoBuff

    def set_device(self, x):
        self._Device = x

    def set_farming(self, x):
        self._Farming = x

    def set_autobuff(self, x):
        self._AutoBuff = x


Setup = CurrentSetup()


def begin_farming(device, farming, autobuff, start):
    def create_monster_list(monster_directory):
        sml = []
        path = glob.glob(monster_directory)
        for img in path:
            sml.append(img)
        return sml

    def get_screenshot(selected_window):
        if selected_window:
            pag.press("alt")
            window = win.FindWindow(None, selected_window)
            if window:
                win.SetForegroundWindow(window)
                x, y, x1, y1 = win.GetClientRect(window)
                x, y = win.ClientToScreen(window, (x + 240, y + 240))
                x1, y1 = win.ClientToScreen(window, ((x1 - 240) - x, (y1 - 240) - y))
                screenshot = pag.screenshot("CurrentScreenshot.png", region=(x, y, x1, y1))
                return screenshot
        else:
            print("invalid Source")
            return None

    def found_monster(_monster):
        ShortString = str(_monster).rsplit("\\", 1)
        No_PNG = ShortString[1].rsplit('.', 1)
        No_Num = ''.join([i for i in No_PNG[0] if not i.isdigit()])
        print('\033[93m' + "Looking for " + str(No_Num) + '\033[0m')
        get_screenshot(device)
        mi = c.imread('CurrentScreenshot.png')
        gmi = c.cvtColor(mi, c.COLOR_BGR2GRAY)
        s = c.imread(_monster, 0)
        width, height = s.shape[:2]
        match_checker = c.matchTemplate(gmi, s, c.TM_CCOEFF_NORMED)
        accuracy = .85
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
                print(Scripts.Colors.Colors.OK_GREEN + No_Num + " Was Found!" + Scripts.Colors.Colors.END_C)
                pag.moveTo(center_cords[0] + width, center_cords[1] + height, duration=.2)
                fx, fy = pag.position()
                pag.click(fx + random.uniform(0, 1.0), fy + random.uniform(0, 1), duration=.2)
                c.imwrite("detected.png", mi)
                return True
            else:
                return False

    while farming:
        for Monsters in create_monster_list(r"Monsters\*.png"):
            current_time = datetime.now()
            if keyboard.is_pressed('p'):
                os.system("pause")

            if found_monster(Monsters):
                # Hit Continue Button
                pag.moveTo(Scripts.Buttons.Buttons.CBL[0], Scripts.Buttons.Buttons.CBL[1], duration=.6)

                pag.click(Scripts.Buttons.Buttons.CBL[0] + random.uniform(1.0, 10.0),
                          Scripts.Buttons.Buttons.CBL[1] + random.uniform(.01, 1), duration=.1)
                # Hit Attack Button
                pag.click(Scripts.Buttons.Buttons.ABL[0] + random.uniform(10, 30),
                          Scripts.Buttons.Buttons.ABL[1] + random.uniform(1.0, 5.0), duration=.8)
                # Hit Attack Button
                pag.click(Scripts.Buttons.Buttons.ABL[0] + random.uniform(3.0, 10.0),
                          Scripts.Buttons.Buttons.ABL[1] + random.uniform(1.0, 5.0), duration=5)

                pag.click(Scripts.Buttons.Buttons.DBL[0] + random.uniform(10, 30),
                          Scripts.Buttons.Buttons.DBL[1] + random.uniform(1.0, 5.0), duration=1.2)
                # Hit Victory Button
                pag.click(Scripts.Buttons.Buttons.VBL[0] + random.uniform(1.0, 20),
                          Scripts.Buttons.Buttons.VBL[1] - 15, duration=3)
                # Hit Heal Button
                pag.click(Scripts.Buttons.Buttons.HBL[0] + random.uniform(1.0, 8.0),
                          Scripts.Buttons.Buttons.HBL[1] + random.uniform(1.0, 8.0), duration=.8)

                # Hit Mana Button
                pag.click(Scripts.Buttons.Buttons.PBL[0] + random.uniform(1.0, 5.0),
                          Scripts.Buttons.Buttons.PBL[1] + random.uniform(1.0, 1.3), duration=1.2)

                # Hit 'x' Button
                pag.click(Scripts.Buttons.Buttons.XBL[0] + random.uniform(1.0, 5.0),
                          Scripts.Buttons.Buttons.XBL[1] + random.uniform(1.0, 5.0), duration=1)

            if autobuff:
                if start.hour + 1 == current_time.hour:
                    if start.minute == current_time.minute:
                        print(Scripts.Colors.Colors.WARNING +
                              "REBUFFING STATEMENT REACHED" + Scripts.Colors.Colors.END_C)
                        Scripts.Rebuff.xp_buff()
                        start = datetime.now()


def main():
    Start_time = datetime.now()
    print(Scripts.Colors.Colors.OK_BLUE + "Starting Time: " + str(Start_time) + Scripts.Colors.Colors.END_C)
    Device = (input("Enter Device Model:\n"))
    Setup.set_device(Device)
    Autobuff = (input("Enable Autobuff? True or False\n"))
    Setup.set_farming(Autobuff)

    Farming = (input("Enable Farming? True or False\n"))
    Setup.set_farming(Farming)
    if Setup.get_farming() == "True":
        print('\033[92m' + "----------Beginning Script.-----------" + '\033[0m')
        begin_farming(Setup.get_device(), Setup.get_farming(), Setup.get_autobuff(), Start_time)

    else:
        print('\033[91m' + "Process Done, Ending Script." + '\033[0m')


if __name__ == "__main__":
    main()
