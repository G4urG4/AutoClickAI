import pyautogui
import time

# import pyscreeze


# Mover el mouse a una posición (x, y)
pyautogui.moveTo(100, 100)

# Hacer clic en la posición actual del mouse
pyautogui.click()

time.sleep(5)
# Arrastrar el mouse a una nueva posición (x, y)
pyautogui.dragTo(200, 200)

# Tomar una captura de pantalla
# screenshot = pyautogui.screenshot()
# screenshot.save("screenshot.png")
