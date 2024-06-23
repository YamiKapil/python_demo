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

# grabbing the text..
successText = driver.find_element(by=By.CLASS_NAME, value="alert-success").text
print(successText)

# sales force login..
driver.get("https://login.salesforce.com")

# generating css from id and class
# tagName#id eg: input#username or #username (only for id)
# tagName.className eg: input.password or .password (only for class)
driver.find_element(by=By.CSS_SELECTOR, value="#username").send_keys("UserName")
driver.find_element(by=By.CSS_SELECTOR, value=".password").send_keys("Pass")
# to clear any data from the field
driver.find_element(by=By.CSS_SELECTOR, value=".password").clear()

# link text the element should start wht <a> tag
driver.find_element(by=By.LINK_TEXT, value="Forgot Your Password?").click()
# getting the element with text using xPath
# driver.find_element(by=By.XPATH, value="//a[text()='Cancel']").click()





