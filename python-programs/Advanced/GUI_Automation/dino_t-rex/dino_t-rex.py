import os, time
import pyautogui
import threading
from selenium import webdriver



os.chdir(r'D:\Knowledge\Python\git\python-programs\Advanced\GUI_Automation\dino_t-rex')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--disable-extensions")

chrome_browser = webdriver.Chrome(executable_path=r'D:\Knowledge\Python\git\python-programs\Advanced\WebBrowser\chromedriver_win32\chromedriver.exe', options=chrome_options)
chrome_browser.maximize_window()

chrome_browser.get('chrome://dino/')

time.sleep(5)
pyautogui.moveTo(1335, 80)
pyautogui.click()
pyautogui.click()

pyautogui.press('space')

def check_for_jump():
    print('check_for_jump called')
    pyautogui.press('f10')
    if pyautogui.locateOnScreen('1.png') != None:
        pyautogui.press('f10')
        pyautogui.press('space')

while True:
    t = threading.Timer(2, check_for_jump)
    t.start()

""" while True:
    pyautogui.press('space')

while True:
    if pyautogui.locateOnScreen('1.png') != None:
        time.sleep(0.2) """

    

""" while True:
    pyautogui.press('f10')
    if pyautogui.locateOnScreen('1.png') != None:
        print('y')
        time.sleep(0.5)
        pyautogui.press('space')
    else:
        print('n' )
    pyautogui.press('f10') """


""" time.sleep(10)         
chrome_browser.quit() """