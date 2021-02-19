from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
time.sleep(3)
driver.quit()