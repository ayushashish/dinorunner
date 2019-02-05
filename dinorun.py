from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
print ("working...")
flag=1
def imageGrab():
    box=(332,408,397,452)
    image= ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a=array (grayImage.getcolors())
    print (a.sum())
    return (a.sum())

def main():
    #flag=1
    while True:
        z=(imageGrab())
        """if (z==3115):
            flag=0
        if (z==3115):
            flag=1"""
        if(z!=3115):
            pyautogui.keyDown('up')
            #time.sleep(0.000001)
            #print ((imageGrab()))
            #pyautogui.keyUp ('up')
            #time.sleep(0.0000001)
            #pyautogui.keyDown('up')
            #pyautogui.keyUp('up')
main ()
