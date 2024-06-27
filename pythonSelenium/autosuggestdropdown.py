import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(by=By.ID, value="autosuggest").send_keys("aus")
time.sleep(2)

# build one common css to get all the options of the dropdown
# li[class='ui-menu-item'] a
listItems = driver.find_elements(by=By.CSS_SELECTOR, value="li[class='ui-menu-item'] a")
print(len(listItems))

for item in listItems:
    print(item.text)
    if item.text == "Austria":
        item.click()
        break  # end the for loop once the item is found
# cannot grab dropdown text like this
print(driver.find_element(by=By.ID, value="autosuggest").text)
# cannot grab text like this from the dropdown as the page will not refresh
# after clicking the dropdown item
# so another method is to get the attribute since it store the value
clickedDropDown = driver.find_element(by=By.ID, value="autosuggest").get_attribute("value")
print(clickedDropDown)
assert clickedDropDown == "Austria"

