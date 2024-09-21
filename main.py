import pyautogui
import time
import reproduzirSom
import botao

# Localização indicando se está esgotado ou não
x = 1278
y = 788

while True:
    time.sleep(2)
    pyautogui.press('f5')
    time.sleep(2)
    #pyautogui.press('f3')
    #time.sleep(1)

    if botao.botaoativo(x, y):

        # Clicks para a quantidade de ingressos
        pyautogui.click(x=1302, y=825, clicks=5)

        # Click para abrir o modal
        pyautogui.click(x=1296, y=999)

        # Clicks para confirmar
        time.sleep(2)
        pyautogui.click(x=1114, y=749)
        pyautogui.click(x=641, y=758)
        pyautogui.click(x=1140, y=819)

        time.sleep(3)

        if botao.compraSucesso(x=883, y=626):
            reproduzirSom.reproduzirmusica()
            break
