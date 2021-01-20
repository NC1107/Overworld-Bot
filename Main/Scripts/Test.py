import cv2
import pyautogui

while True:
    X, Y = pyautogui.position()

    cv2.waitKey(1000)

    #     # print(pyautogui.pixel(X, Y))
    print(("X: " + str(X) + " Y: " + str(Y)))
