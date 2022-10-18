from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('./Drivers/chromedriver')
driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, 'q')
search_bar.clear()
search_bar.send_keys('getting started with python')
search_bar.send_keys(Keys.RETURN)




print('\nThe current url is : {}\n'.format(driver.current_url))

driver.close()