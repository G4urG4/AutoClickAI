import pyautogui
import time
import random


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
    # pyautogui.click()


def moveMouse(arrDstr=[], posR_B=[]):
    if len(arrDstr) == 0:
        print("Ingresa una cantidad")
        return exit
    nC = sum(arrDstr)
    print(nC)
    rowXcolumn = [12, 3]
    # SqrGree
    posGreeInit = [[680, 700], [705, 850]]
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
    for i in range(rowXcolumn[0]):
        for j in range(rowXcolumn[1]):
            coorandX = random.randint(posX + 10, posX + dismRecT[0] - 15)
            coorandY = random.randint(posY + 10, posY + dismRecT[1] - 15)
            dictValuesC.append([coorandX, coorandY])
            posY -= dismRecT[1]
        posX += dismRecT[0]
        posY = posInit[1]

    nCmov = []
    iW_one = 0
    jW_one = 0
    perFSqrt = [0] + list(map(lambda x: x - 1, posR_B))
    perFSqrt_T = [0, 12, 24, 36]
    conI = 1
    while iW_one < nC:
        valorRC = random.randint(perFSqrt_T[conI - 1], perFSqrt[conI])
        if valorRC not in nCmov:
            nCmov.append(valorRC)
            iW_one += 1
            jW_one += 1
            if jW_one == arrDstr[conI - 1]:
                jW_one = 0
                conI += 1
    nCmov.sort()
    iW_two = 0
    average_time = 13
    time_per_Move = [random.random() for _ in range(nC)]
    current_sum = sum(time_per_Move)
    time_per_Move = [x * average_time / current_sum for x in time_per_Move]

    while iW_two < nC:
        pyautogui.moveTo(dictValuesC[nCmov[iW_two]][0], dictValuesC[nCmov[iW_two]][1])
        # pyautogui.click()
        # pyautogui.dragTo(300, 300)
        print(
            f"i:{iW_two}({nCmov[iW_two]+1})(t:{time_per_Move[iW_two]:.3f})->x:{dictValuesC[nCmov[iW_two]][0]},y:{dictValuesC[nCmov[iW_two]][1]}"
        )
        time.sleep(time_per_Move[iW_two])
        iW_two += 1
    print(f"Tiempor promedio {sum(time_per_Move)}")


def mixFunctionC():
    percentageArr = [100, 0, 0, 0, 0]  # [moneda,SinFondos,HasGanado,CashPa,errInes]
    valorIndex = []
    for i in range(len(percentageArr)):
        if percentageArr[i] == 100:
            valorIndex.append(i)
    if len(valorIndex) > 1:
        skipNotification(valorIndex)
    if len(valorIndex) == 1 and valorIndex[0] != 0:
        skipNotification(valorIndex)
    if valorIndex[0] == 0 and len(valorIndex) == 1:
        moveMouse([8, 8, 7], [12, 24, 36])
        # time.sleep(4)
        # pyautogui.moveTo(300, 400)


mixFunctionC()
