from datetime import datetime
import time
import pyautogui as pag
import random
import Scripts.Colors
import Scripts.Buttons


def xp_buff():
    # Console printout for rebuff
    print(Scripts.Colors.Colors.FAIL + "--REBUFFING--" + Scripts.Colors.Colors.END_C)

    # button location & movement scripts to rebuff
    pag.click(Scripts.Buttons.Buttons.HBL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.HBL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.EXP[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.EXP[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.LCL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.LCL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.SCL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.SCL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.OCL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.OCL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.ACL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.ACL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.TL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.TL[1] + random.uniform(1.0, 5.0), duration=1)
    pag.click(Scripts.Buttons.Buttons.XBL[0] + random.uniform(1.0, 5.0),
              Scripts.Buttons.Buttons.XBL[1] + random.uniform(1.0, 5.0), duration=1)
