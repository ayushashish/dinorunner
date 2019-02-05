from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
print ("working...")

def imageGrab():
    box=(332,408,397,452)
    image= ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a=array (grayImage.getcolors())
    print (a.sum())
	#the actual value can be checked here
    return (a.sum())

def main():
    while True:
        z=(imageGrab())
        if(z!=3115):#or the value obtained above
            pyautogui.keyDown('up')
main ()

