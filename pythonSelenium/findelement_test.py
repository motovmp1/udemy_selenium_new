from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.makemytrip.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(1)
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@id='fromCity']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")
time.sleep(2)
# cities = driver.find_elements_by_css_selector("p[class*='appendBottom5']")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
for index, city in enumerate(cities):
    print(index, "--> " + city.text)

# close all navigator here
time.sleep(2)
driver.close()
