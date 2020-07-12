from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(1)
driver.implicitly_wait(10)

element = driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnI']")
print(element.get_attribute('value'))