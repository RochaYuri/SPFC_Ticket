import pyautogui

def botaoativo(x, y):
    pixel_color = pyautogui.pixel(x, y)

    if pixel_color != (214, 17, 0):
        return True
    else:
        return False
