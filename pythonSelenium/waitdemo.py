import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# the implicit wait is attached to the driver itself
# So it applies to all the elements
# driver.implicitly_wait(5)  # do not wait 3sec if the element is found before 3 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise")

searchBox = driver.find_element(by=By.CLASS_NAME,value="search-keyword")
searchBox.send_keys("ber")
time.sleep(2)
addedProducts = []
# searchedProducts = driver.find_elements(by=By.XPATH, value="//div[@class='products']/div")
# for products in searchedProducts:
#     productName = products.find_element(by=By.CLASS_NAME, value="product-name")
#     addedProducts.append(productName.text)
#     # print(productName.text)

buttons = driver.find_elements(by=By.XPATH, value="//div[@class='product-action']/button")
# selecting the buttons to add to cart
for items in buttons:
    # go up the parent div to get the product name using xPath
    # traversing up to the parent
    productName = items.find_element(by=By.XPATH, value="parent::div/parent::div/h4")
    addedProducts.append(productName.text)
    items.click()


# opening the cart and adding to check out
driver.find_element(by=By.CSS_SELECTOR, value="img[alt='Cart']").click()
time.sleep(1)
checkoutButton = driver.find_element(by=By.XPATH, value="//div[@class='action-block']/button")
checkoutButton.click()
# explict wait
wait = WebDriverWait(driver,6)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))
# checkout screen adding promo code and checkout
checkProducts = driver.find_elements(by=By.XPATH, value="//p[@class='product-name']")
otherList = []
for prod in checkProducts:
    otherList.append(prod.text)

assert addedProducts == otherList
totalBeforeDiscount = driver.find_element(by=By.CLASS_NAME, value="discountAmt").text
driver.find_element(by=By.CLASS_NAME, value="promoCode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR, value=".promoBtn").click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promoAppliedText = driver.find_element(by=By.CLASS_NAME, value="promoInfo")
print(promoAppliedText.text)
totalAfterDiscount = driver.find_element(by=By.CLASS_NAME, value="discountAmt").text
assert float(totalBeforeDiscount) > float(totalAfterDiscount)

# checking if the total amount matches with the sum
totalAmount = 0
amounts = driver.find_elements(by=By.XPATH, value="//tr/td[5]/p")
sumAmount = driver.find_element(by=By.CLASS_NAME, value="totAmt").text
for amount in amounts:
    totalAmount = totalAmount + int(amount.text)

assert int(totalAmount) == int(sumAmount)








