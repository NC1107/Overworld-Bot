import win32gui as win
import pyautogui as pag


def get_screenshot(selected_window):
    if selected_window:
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
