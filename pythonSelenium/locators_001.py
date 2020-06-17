from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

time.sleep(3)
driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").send_keys("Vinicius Miranda de Pinho")
time.sleep(1)
driver.find_element_by_name("email").send_keys("vinicius.mpinho@gmail.com")
time.sleep(1)
driver.find_element_by_id("exampleInputPassword1").send_keys("123mudar")
driver.find_element_by_id("exampleCheck1").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
time.sleep(2)

drop_down = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
drop_down.select_by_visible_text("Female")

message_alert = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(message_alert)
time.sleep(1)
assert "Success!" in message_alert

# close all navigator
time.sleep(4)
driver.close()
