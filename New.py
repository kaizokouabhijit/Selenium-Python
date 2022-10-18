from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./Drivers/chromedriver')
driver.get("https://www.python.org")



print('The current url is : {}'.format(driver.current_url))

# driver.close()