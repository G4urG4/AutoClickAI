import pyautogui
import time
from PIL import Image
import numpy as np
import pandas as pd
import random

# import pyscreeze


def valoresImg():
    # Cargar la imagen
    image_path = "./principal_pantalla.jpg"
    image = Image.open(image_path)
    # Convertir la imagen a escala de grises (opcional)
    image = image.convert("L")
    # Convertir la imagen a una matriz numpy
    image_array = np.array(image)
    # Crear un DataFrame de pandas a partir de la matriz
    df = pd.DataFrame(image_array)
    # Guardar el DataFrame en un archivo CSV
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


def moveMouse(nC):
    # posInit = [715, 705]
    posInit = [715, 805]
    dismRecT = [40, 50]
    posX = posInit[0]
    posY = posInit[1]
    dictValuesC = []
    for i in range(len(a[0])):
        for j in range(len(a)):
            coorandX = random.randint(posX + 10, posX + dismRecT[0] - 15)
            coorandY = random.randint(posY + 10, posY + dismRecT[1] - 15)
            # pyautogui.moveTo(coorandX, coorandY)
            # time.sleep(1)
            dictValuesC.append([coorandX, coorandY])
            posY -= dismRecT[1]
        posX += dismRecT[0]
        posY = posInit[1]

    # for j in range(len(a)):
    #     for i in range(len(a[0])):
    #         coorandX = random.randint(posX + 10, posX + dismRecT[0] - 15)
    #         coorandY = random.randint(
    #             posInit[1] + 10, posInit[1] + dismRecT[1] - 5 - 10
    #         )
    #         dictValuesC.append([coorandX, coorandY])
    #         posX += dismRecT[0]
    #     posInit[1] += dismRecT[1]
    #     posX = posInit[0]

    nCmov = []
    iW_one = 0
    while iW_one < nC:
        valorRC = random.randint(0, 31)
        if valorRC not in nCmov:
            nCmov.append(valorRC)
            iW_one += 1
    iW_two = 0
    while iW_two < nC:
        pyautogui.moveTo(dictValuesC[nCmov[iW_two]][0], dictValuesC[nCmov[iW_two]][1])
        print(
            f"i:{iW_two}({nCmov[iW_two]+1})->x:{dictValuesC[nCmov[iW_two]][0]},y:{dictValuesC[nCmov[iW_two]][1]}"
        )
        time.sleep(1)
        iW_two += 1

    # pyautogui.click()
    # Arrastrar el mouse a una nueva posición (x, y)
    # pyautogui.dragTo(300, 300)
    # Tomar una captura de pantalla
    # screenshot = pyautogui.screenshot()
    # screenshot.save("screenshot.png")


moveMouse(24)
# valoresImg()
