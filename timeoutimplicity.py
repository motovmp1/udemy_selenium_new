from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

start = datetime.now().replace(microsecond=0)

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.set_window_size(1450, 800)


driver.get("https://jsfiddle.net/davidThomas/DGbT3/3")
driver.implicitly_wait(20)
url1 = driver.current_url
print(url1)

test = driver.find_element_by_xpath("//iframe[@name='result']")

driver.find_element_by_id("run").click()

driver.switch_to.frame("result")

time.sleep(2)
print("Step 1 - Inside the elements")
source3 = driver.find_element_by_css_selector("#dragThis")
target3 = driver.find_element_by_css_selector("#dropHere")

print("Step 2 - Inside the drag and drop")
actions = ActionChains(driver)
actions.drag_and_drop(source3, target3)
actions.perform()

# fechae o browser
driver.quit()
print(f' time total for UUT is:  {datetime.now().replace(microsecond=0) - start}')
