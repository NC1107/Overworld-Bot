import pyautogui as pag
import win32api as win
from os import path

NoClick = win.GetKeyState(0x01)
while True:
    a = win.GetKeyState(0x01)


    def add_monster():
        x, y = pag.position()
        monster_logo = pag.screenshot(region=(x - 6, y - 6, 12, 12))
        save_file = str(input("Enter the monster name:\n"))
        file_name = 'C:\\Users\\Nick Conn\\Documents\\GitHub\\Overworld-Bot\\Main\\ScaledMonsters' + '\\' + save_file \
                    + '.png'
        count = 0
        while path.exists(file_name):
            count += 1
            file_name = 'C:\\Users\\Nick Conn\\Documents\\GitHub\\Overworld-Bot\\Main\\ScaledMonsters' + '\\' \
                        + save_file + str(count) + '.png'

        monster_logo.save(file_name)
        print("Saved as: " + file_name)


    if a != NoClick:
        add_monster()
