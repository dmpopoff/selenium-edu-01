from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/admin")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_name("login").click()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
sleep(2)

countries = driver.find_elements_by_css_selector("td:nth-child(5) > a")
print("number of countries is", len(countries))
# for country in countries:
#     print(country.get_attribute("textContent"))
if all(countries[i].get_attribute("textContent") <= countries[i+1].get_attribute("textContent") for i in range(len(countries)-1)):
    print("Countries are in alphabetical order.")

driver.quit()