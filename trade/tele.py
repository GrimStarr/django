from asyncio.windows_events import NULL
from ctypes import resize
from turtle import heading, width
import pygetwindow
import pyautogui
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def getIName(name):
    value = Image.open(name)
    text = tess.image_to_string(value, config='')
    return text


def screenshot():

    path = "/"

    titles = pygetwindow.getAllTitles()

    # x1,y1,width,height = pygetwindow.getWindowGeometry('Telegram')
    tt = pygetwindow.getWindowsWithTitle('Telegram')

    # pyautogui.screenshot('telegram.png', region=(30, 309, 375, 160))
    pyautogui.screenshot('telegram2.png', region=(30, 550, 400, 130))

    # img = Image.open('telegram.png')
   # print(img.height, " ", img.width)
    # resized = img.resize((300, 120))
    # resized.save('telegram.png')

    img = Image.open('telegram2.png')
  #  print(img.height, " ", img.width)
    resized = img.resize((700, 240))
    resized.save('telegram2.png')

    varray = ["XAUUSD"]
    # vsymbol = getIName('telegram.png').replace(
        # " ", "").replace("/", "").replace("\n", "")

    # varray.append(vsymbol)
    var = getIName('telegram2.png')
    print(var)
    try:
        varType = var.find("Gold") + 5
        varTP = var.find("TP") + 3
        varSL = var.find("S") + 5
        varCur = var.find("@") + 2
        valueType = var[varType:varType+4].replace(" ","")
        valueSL = var[varSL:varSL+7]
        varTParray = var[varTP:varTP+23].replace("/", " ").split()
        valueCur = var[varCur:varCur+7]

        varray.append(valueType)
        varray.append(valueCur)
        varray.extend(varTParray)
        varray.append(valueSL)
        varray.insert(3,"TP")
        varray.insert(5,"TP")
        varray.insert(7,"TP")
        varray.insert(9,"SL")

        return varray
    except Exception as err:
        return NULL
        print("tele error: ", err)

    


# screenshot()
