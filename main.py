import pyautogui
import time
import reproduzirSom
import botao

# Localização indicando se está esgotado ou não
x = 1376
y = 568

while True:
    time.sleep(5)
    pyautogui.press('f5')
    time.sleep(2)
    pyautogui.press('f3')
    time.sleep(1)

    if botao.botaoativo(x, y):

        # Clicks para a quantidade de ingressos
        pyautogui.click(x=1299, y=575, clicks=5)

        # Click para abrir o modal
        pyautogui.click(x=1393, y=985)

        # Clicks para confirmar
        time.sleep(2)
        pyautogui.click(x=1100, y=754)
        pyautogui.click(x=656, y=753)
        pyautogui.click(x=1122, y=811)
        reproduzirSom.reproduzirmusica()
        break
