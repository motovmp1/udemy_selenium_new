from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#chrome_options.add_argument("--disable-extensions")

#chrome_options.add_argument("--disable-gpu")

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

start_url = "https://google.com"

driver.get(start_url)

print(driver.current_url)

driver.quit()
driver.find_element_by_xpath("").click()
driver.find_element_by_xpath("").send_keys()