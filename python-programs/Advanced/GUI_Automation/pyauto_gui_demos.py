import pyautogui
import time
import os

os.chdir(r'D:\Knowledge\Python\git\python-programs\Advanced\GUI_Automation')
pyautogui.screenshot('Taken_screenshot.png')

exit()

width,height = pyautogui.size() # returns screen resolution

print(pyautogui.position()) # current cordinates

pyautogui.moveTo(50,50, duration=1) # move mouse cursor
pyautogui.moveRel(900,300, duration=1)
pyautogui.scroll(clicks=200)

time.sleep(5)

pyautogui.click()    # click to put drawing program in focus

distance = 50
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

time.sleep(5)

pyautogui.typewrite('Hello world !', interval=0.2)

#print(pyautogui.KEYBOARD_KEYS)
#pyautogui.press('f1', interval=2)
#pyautogui.hotkey('ctrl', 'alt', 'n')

