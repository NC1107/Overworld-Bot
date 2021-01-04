import pyautogui as PAG
import win32api as Win
from os import path

NoClick = Win.GetKeyState(0x01)
while True:
    a = Win.GetKeyState(0x01)


    def AddMonster():
        x, y = PAG.position()
        MonsterLogo = PAG.screenshot(region=(x - 6, y - 6, 12, 12))
        SaveFile = str(input("Enter the monster name:\n"))
        FileName = 'C:\\Users\\18862\\Desktop\\Overworld Bot\\Main\\ScaledMonsters' + '\\' + SaveFile + '.png'
        Count = 0
        while path.exists(FileName):
            Count += 1
            FileName = 'C:\\Users\\18862\\Desktop\\Overworld Bot\\Main\\ScaledMonsters' + '\\' \
                       + SaveFile + str(Count) + '.png'

        MonsterLogo.save(FileName)
        print("Saved as: " + FileName)


    if a != NoClick:
        AddMonster()
