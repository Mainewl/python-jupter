
import os
import pyautogui
import time

os.startfile('https://outlook.live.com/mail/0/AQMkADAwATY3ZmYAZS1kYWVkLTBhYmEtMDACLTAwCgAuAAAD54YNaEZW2UCevKtOsSeOOAEAZdQx9jNvnU2mBeJG5jk46AAFMPcE7wAAAA%3D%3D/id/AQMkADAwATY3ZmYAZS1kYWVkLTBhYmEtMDACLTAwCgBGAAAD54YNaEZW2UCevKtOsSeOOAcAZdQx9jNvnU2mBeJG5jk46AAFMPcE7wAAAGXUMfYzb51NpgXiRuY5OOgABTD3YysAAAA%3D')

monita = pyautogui.size()
print (monita)

mous = pyautogui.position()
print (mous)

time.sleep(5)

pyautogui.click(x=110, y=233)
time.sleep(2)

pyautogui.click(x=564, y=712)
time.sleep(15)

pyautogui.click(x=622, y=521)
time.sleep(1)

pyautogui.click('https://forms.office.com/Pages/DesignPage.aspx#FormId=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAYAAKU3xH9UMVE0SjFLRVc4VjJSM1A1REZFQ0pYRlFPVy4u&Analysis=true')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/#chrome")
driver.quit()