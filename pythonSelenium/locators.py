from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice")

# find element by name
driver.find_element(by=By.NAME, value="name").send_keys("Hello")

# find element by css selector
driver.find_element(by=By.CSS_SELECTOR, value="input[name='name']").send_keys("hello")

# find element by id
driver.find_element(by=By.ID, value="exampleCheck1").click()

# find element by xPath
driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()



