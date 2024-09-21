import pyautogui

def botaoativo(x, y):
    pixel_color = pyautogui.pixel(x, y)
    print(pixel_color)
    if pixel_color != (214, 17, 0):
        return True
    else:
        return False

def compraSucesso(x, y):
    pixel_color = pyautogui.pixel(x, y)
    print(pixel_color)
    if pixel_color != (175, 7, 13):
        return True
    else:
        return False
