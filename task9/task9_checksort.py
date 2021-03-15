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
countries_num = len(countries)
print("number of countries is", countries_num)
# for country in countries:
#     print(country.get_attribute("textContent"))
if all(countries[i].get_attribute("textContent") <= countries[i+1].get_attribute("textContent") for i in range(len(countries)-1)):
    print("Countries are in alphabetical order.")
else:
    print("Countries are NOT in alphabetical order.")
countries_rows = driver.find_elements_by_css_selector("tr.row > td:nth-child(6)")
for country_row in range(len(countries_rows)):
    # print(country_row+2)
    country = driver.find_element_by_css_selector("tr.row:nth-child("+str(country_row+2)+")")
    zones_count = country.find_element_by_css_selector("td:nth-child(6)").get_attribute("textContent")
    print("zones count", zones_count)
    if int(zones_count) > 0:
        country.find_element_by_css_selector("td:nth-child(5) > a").click()
        print(driver.find_element_by_css_selector("tr > td:nth-child(3)").get_attribute("textContent"))
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        time(0.5)

# print(countries_rows[0].get_attribute("textContent"))
# показать 4ую страну. use 5 for 4
# country4 = driver.find_elements_by_css_selector("tr.row:nth-child(5)")
# print("четвертая страна -", country1[0].find_element_by_css_selector("td:nth-child(5) > a").get_attribute("textContent"))
driver.quit()