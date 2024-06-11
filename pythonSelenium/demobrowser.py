from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# invoking browser to start testing
# browser exposes an executable file
# through selenium test we need to invoke the executable file which will
# then invoke actual browser
# chrome_driver_path = "D:\\chromedriver.exe"
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.close()  # close the driver manually
driver = webdriver.Chrome() # run in chrome
# driver = webdriver.Ie()  # for Internet Explorer
# driver.maximize_window() # open the browser in maximize mode
driver.get('https://www.google.com/')  # get method to hit url in browser

# print(driver.title)
# print(driver.current_url)
driver.get('https://aniwave.to/home')  # go to new url
driver.back()  # go back to previous screen
driver.refresh() # refresh the current screen
