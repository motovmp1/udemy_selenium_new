from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_behave.hooks import allure_report


@given('launch chrome browser')
def test_launchBrowser(context):
    # here you can add your path for Chromedriver in case you have your path
    # context.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    # My Chromedriver located in Environment windows by default.
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    time.sleep(2)


@when('open orange hrm homepage')
def test_OpenHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(2)


@then('verify that the logo present on page')
def test_verifylogo(context):
    status_page = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    time.sleep(2)
    assert status_page is True


@then('Close browser')
def test_closebrowser(context):
    time.sleep(2)
    context.driver.close()


allure_report("C:/Users/elsys/Documents/pycharm_robot/udemy_selenium/features/reports")
