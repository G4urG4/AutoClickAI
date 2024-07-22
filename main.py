import pyautogui
import time
from PIL import Image
import numpy as np
import pandas as pd
import random


def valoresImg():
    image_path = "./principal_pantalla.jpg"
    image = Image.open(image_path)
    image = image.convert("L")
    image_array = np.array(image)
    df = pd.DataFrame(image_array)
    csv_path = "./valorImg.csv"
    df.to_csv(csv_path, index=False, header=False)
    print(f"La imagen ha sido convertida y guardada en {csv_path}")


a = [
    {
        "3": [1, 0],
        "6": [2, 0],
        "9": [3, 0],
        "12": [4, 0],
        "15": [5, 0],
        "18": [6, 0],
        "21": [7, 0],
        "24": [8, 0],
        "27": [9, 0],
        "30": [10, 0],
        "33": [11, 0],
        "36": [12, 0],
    },
    {
        "2": [1, 1],
        "5": [2, 1],
        "8": [3, 1],
        "11": [4, 1],
        "14": [5, 1],
        "17": [6, 1],
        "20": [7, 1],
        "23": [8, 1],
        "26": [9, 1],
        "29": [10, 1],
        "32": [11, 1],
        "35": [12, 1],
    },
    {
        "1": [1, 2],
        "4": [2, 2],
        "7": [3, 2],
        "10": [4, 2],
        "13": [5, 2],
        "16": [6, 2],
        "19": [7, 2],
        "22": [8, 2],
        "25": [9, 2],
        "28": [10, 2],
        "31": [11, 2],
        "34": [12, 2],
    },
]


def skipNotification(perC):
    xorOpt = random.randint(0, 1)
    tVrand = []
    valSpam = -1
    if len(perC) > 1:
        valSpam = perC[1]
    if len(perC) == 1:
        valSpam = perC[0]

    if valSpam == 1:
        if xorOpt == 0:
            valorInit = [[810, 1100], [630, 655]]
        else:
            valorInit = [[1092, 1100], [538, 548]]
    if valSpam == 2:
        valorInit = [[840, 1060], [660, 695]]
    if valSpam == 3:
        valorInit = [[845, 1060], [800, 835]]
    if valSpam == 4:
        if xorOpt == 0:
            valorInit = [[808, 1095], [655, 680]]
        else:
            valorInit = [[1092, 1100], [550, 558]]

    tVrand = [
        random.randint(valorInit[0][0], valorInit[0][1]),
        random.randint(valorInit[1][0], valorInit[1][1]),
    ]
    pyautogui.moveTo(tVrand[0], tVrand[1])


def moveMouse(nC):
    # SqrGree
    posGreeInit = [[680, 710], [705, 850]]
    tVrand = [
        random.randint(posGreeInit[0][0], posGreeInit[0][1]),
        random.randint(posGreeInit[1][0], posGreeInit[1][1]),
    ]
    pyautogui.moveTo(tVrand[0], tVrand[1])
    # pyautogui.click()
    # AllSquares
    posInit = [715, 805]
    dismRecT = [40, 50]
    posX = posInit[0]
    posY = posInit[1]
    dictValuesC = []
    for i in range(len(a[0])):
        for j in range(len(a)):
            coorandX = random.randint(posX + 10, posX + dismRecT[0] - 15)
            coorandY = random.randint(posY + 10, posY + dismRecT[1] - 15)
            dictValuesC.append([coorandX, coorandY])
            posY -= dismRecT[1]
        posX += dismRecT[0]
        posY = posInit[1]

    nCmov = []
    iW_one = 0
    while iW_one < nC:
        valorRC = random.randint(0, 35)
        if valorRC not in nCmov:
            nCmov.append(valorRC)
            iW_one += 1
    nCmov.sort()
    iW_two = 0
    while iW_two < nC:
        pyautogui.moveTo(dictValuesC[nCmov[iW_two]][0], dictValuesC[nCmov[iW_two]][1])
        # pyautogui.click()
        print(
            f"i:{iW_two}({nCmov[iW_two]+1})->x:{dictValuesC[nCmov[iW_two]][0]},y:{dictValuesC[nCmov[iW_two]][1]}"
        )
        # time.sleep(1)
        iW_two += 1


def mixFunctionC():
    percentageArr = [100, 0, 0, 0, 0]  # [moneda,SinFondos,HasGanado,CashPa,errInes]
    moveMouse(24)
    valorIndex = []
    for i in range(len(percentageArr)):
        if percentageArr[i] == 100:
            valorIndex.append(i)
    if len(valorIndex) > 1:
        skipNotification(valorIndex)
    if len(valorIndex) == 1 and valorIndex[0] != 0:
        skipNotification(valorIndex)

    # pyautogui.click()
    # pyautogui.dragTo(300, 300)
    # screenshot = pyautogui.screenshot()
    # screenshot.save("screenshot.png")


mixFunctionC()

# valoresImg()
