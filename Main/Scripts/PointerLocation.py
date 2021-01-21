import cv2
import pyautogui

while True:
    X, Y = pyautogui.position()

    cv2.waitKey(1000)

    print(("X: " + str(X) + " Y: " + str(Y)))
