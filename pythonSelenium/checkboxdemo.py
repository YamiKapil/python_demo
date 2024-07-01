from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

checkboxes = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox']")
print(len(checkboxes))

for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()  # click the checkbox
        assert i.is_selected()  # tells if the checkbox is selected or not (true/false)
        break
