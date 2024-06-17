from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)  # initializing the Chrome driver

# driver.get("https://www.google.com/")
# driver.find_element(by=By.ID, value="APjFqb").send_keys("Hello")
# driver.get("https://uat.mo-finance.com/")
driver.get("http://46.250.238.173:3000/")
try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1vccs49")))
    # driver.find_element(by=By.ID, value="email")
    driver.find_element(by=By.ID, value="email").send_keys("admin@neoremit.com")
    driver.find_element(by=By.ID, value="password").send_keys("admin")
    loginButton = driver.find_element(by=By.CLASS_NAME, value="chakra-button.css-i0rzuz")
    loginButton.click()
    # checkbox = driver.find_element(by=By.ID, value="remember")
    # checkbox.click()
    driver.close()
except NoSuchElementException:
    print('element not found')
else:
    print("element exist")


