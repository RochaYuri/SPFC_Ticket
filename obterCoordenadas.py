import pyautogui
import time

# Use Ctrl + C para interromper o loop
try:
    while True:
        x, y = pyautogui.position()
        print(f'Posição: ({x}, {y})')
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrompido")
    