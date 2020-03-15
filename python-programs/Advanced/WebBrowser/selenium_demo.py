from selenium import webdriver
import time

ff_browser = webdriver.Firefox(executable_path=r'D:\Knowledge\Python\git\python-programs\Advanced\WebBrowser\geckodriver-v0.26.0-win64\geckodriver.exe')
#chrome_browser.get('google.com')
#chrome_browser = webdriver.Chrome(executable_path=r'D:\Knowledge\Python\git\python-programs\Advanced\WebBrowser\chromedriver_win32\chromedriver.exe')

ff_browser.get('https://google.com')
img = ff_browser.find_element_by_id('hplogo')
print(img)

search_element = ff_browser.find_elements_by_css_selector('input.gLFyf')[0]
print(search_element)
search_element.click()
search_element.send_keys('Hello')
time.sleep(5) # explicitely wait for 5 seconds, just to see how it works
ff_browser.refresh()
ff_browser.quit()