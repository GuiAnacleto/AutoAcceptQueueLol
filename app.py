import mouse
import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time

acceptButtonImg = './sample.png'
pyautogui.FAILSAFE = False
TIMELAPSE = 1

# Find the image on the screen
def auto_accept():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        print(pos)
        print("Buscando Accept!")
        if not pos[0] == -1:
            mouse.move(pos[0], pos[1])
            mouse.click('left')
            print("Jogo Aceito!")
            break
        
        time.sleep(TIMELAPSE)

auto_accept()
