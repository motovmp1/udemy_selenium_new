from selenium import webdriver
import time

# every browser exposes an executable file, thought selenium
# we ned to invoke exe file such as chrome.
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

driver.maximize_window()

# this is allow to land inside the webapage that you need to access
driver.get("https://rahulshettyacademy.com")

# get the website title if we inside or not
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)
time.sleep(5)
driver.back()
driver.refresh()

# driver close all browser
time.sleep(3)
driver.close()
