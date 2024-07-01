from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.find_element(by=By.CSS_SELECTOR, value="#name").send_keys("Hello")
driver.find_element(by=By.ID, value="alertbtn").click()
windowHandle = driver.window_handles
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()  # to click yes/accept in the alert dialog

# dismiss the alert
# driver.find_element(by=By.CSS_SELECTOR, value="#name").send_keys("Cancel this")
# driver.find_element(by=By.ID, value="confirmbtn").click()
# alert2 = driver.switch_to.alert
# print(alert2.text)
# alert2.dismiss()  # to dismiss/ click cancel in the alert dialog





