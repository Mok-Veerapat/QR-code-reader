import cv2
from tkinter import *
import math as M
import autopy as ap
import pyautogui as pag
from time import sleep
from webbrowser import open
import qrcode

#    Create by programmer name Veerapat 
#    license Free for personal usage
#    Version 0.1
#    was create at 1 / 08 / 2020

#             for more informations  
# https://www.thepythoncode.com/article/generate-read-qr-code-python

''' File name '''
pic_name = "QR_code_test.png"

class progressbar():

    def __init__ (self):
        pass



def working_bar(text="#", caption="Loading... ", woking_time=0.05, times=30):
    for i in range(times):
        mai_string = caption + text*i 
        print(mai_string, end='')
        print('\b' * len(mai_string), end='', flush=True)
        sleep(woking_time)

    sleep(0.5)    
    print("\n Finish :D")

def Input():
    topleft = (0, 0)
    w_h = [1920, 1080]
    rect = []
    while True:
        print("1  Set_TopLeft")
        print("2  Set_bottomRight")
        print("3  leave and capture screen")
        print("4  for Close this program")
        a = int(input("Enter :"))
        if a == 1: 
            topleft = ap.mouse.location()
            print("Topleft is :",topleft)
        elif a == 2:
            bottomright = ap.mouse.location()
            print("bottomright is :",bottomright)
             
            w_h.insert(0,bottomright[0] - int(topleft[0]))
            w_h.insert(1,bottomright[1] - int(topleft[1]))

            print("Width and height is:",tuple(w_h))
        elif a == 3:
            pag.screenshot(region=(topleft[0], topleft[1], w_h[0], w_h[1]), imageFilename=pic_name)

            Read()
            break
        else:
            break
            


def Create():
    data = "https://www.google.com"
    
    file_name = "Google.png"

    QR_img = qrcode.make(data)

    QR_img.save(file_name)


def Read():
    img =  cv2.imread(pic_name)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    print( "data = ",data)

    print("open webbrowser in 3s")
    working_bar(text="@", caption="Process... ", woking_time=0.25, times=12)
    open(data)

    Input()


def Gui():
    root = Tk()
    root.geometry("500x500")

    root.mainloop()


if __name__ == "__main__":

    #Gui()

    working_bar()
    #Create()
    Input()
    

    







