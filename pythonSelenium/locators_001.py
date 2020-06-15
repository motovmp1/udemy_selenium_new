from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

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


# close all navigator
time.sleep(4)
driver.close()

