from selenium import webdriver
from time import sleep
from random import randint

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")
sleep(1)
firstname = "%05d" % randint(0,99999)
lastname = "Popov"
address1 = "Ivanova str, 1"
postcode = firstname
city = "Moscow"
password = "%09d" % randint(0,999999999)
email = firstname+'@1.com'
phone = "+7"+password

print(email, password)
driver.find_element_by_css_selector("form a").click()
sleep(1)
driver.find_element_by_css_selector("input[name=firstname]").send_keys(firstname)
sleep(0.1)
driver.find_element_by_css_selector("input[name=lastname]").send_keys(lastname)
sleep(0.1)
driver.find_element_by_css_selector("input[name=address1]").send_keys(address1)
sleep(0.1)
driver.find_element_by_css_selector("input[name=postcode]").send_keys(postcode)
sleep(0.1)
driver.find_element_by_css_selector("input[name=city]").send_keys(city)
sleep(0.1)
driver.find_element_by_css_selector("span.select2-selection__arrow").click()
sleep(0.5)
driver.find_element_by_css_selector("li.select2-results__option[id$=US]").click()
sleep(0.1)
driver.find_element_by_css_selector("input[name=email]").send_keys(email)
sleep(0.1)
driver.find_element_by_css_selector("input[name=phone]").send_keys(phone)
sleep(0.1)
driver.find_element_by_css_selector("input[name=password]").send_keys(password)
sleep(0.1)
driver.find_element_by_css_selector("input[name=confirmed_password]").send_keys(password)
driver.find_element_by_css_selector("button[name=create_account]").click()
driver.get("http://localhost/litecart/en/logout")
#login
driver.find_element_by_css_selector("input[name=email]").send_keys(email)
sleep(0.1)
driver.find_element_by_css_selector("input[name=password]").send_keys(password)
driver.find_element_by_css_selector("button[name=login]").click()
sleep(4)
driver.get("http://localhost/litecart/en/logout")
driver.quit()