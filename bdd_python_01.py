from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(1)
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)


element = driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnI']")
value_button = element.get_attribute('value')
print(element.get_attribute('value'))

# uma opcao seria colocar lower case
assert "sinto-me com sorte" == value_button.lower()

time.sleep(2)
driver.close()

