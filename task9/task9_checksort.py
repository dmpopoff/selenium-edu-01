from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/admin")
sleep(1)
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
sleep(2)

countries = driver.find_elements_by_css_selector("td:nth-child(5) > a")
countries_num = len(countries)
print("number of countries is", countries_num)
# for country in countries:
#     print(country.get_attribute("textContent"))
print("paragraph 1 subparagraph a")
if all(countries[i].get_attribute("textContent") <= countries[i+1].get_attribute("textContent") for i in range(len(countries)-1)):
    print("Countries are in alphabetical order.")
else:
    print("Countries are NOT in alphabetical order.")
print("paragraph 1 subparagraph b")
countries_rows = driver.find_elements_by_css_selector("tr.row > td:nth-child(6)")
for country_row in range(len(countries_rows)):
    # print(country_row+2)
    country = driver.find_element_by_css_selector("tr.row:nth-child("+str(country_row+2)+")")
    zones_count = int(country.find_element_by_css_selector("td:nth-child(6)").get_attribute("textContent"))
    if int(zones_count) > 0:
        # print("zones count", zones_count)
        country.find_element_by_css_selector("td:nth-child(5) > a").click()
        zones = driver.find_elements_by_css_selector("table.dataTable input[type='hidden'][name *= name]")
        if all(zones[i].get_attribute("value") <= zones[i+1].get_attribute("value") for i in range(zones_count-1)):
            print("Zones are in alphabetical order.")
        else:
            print("Zones are NOT in alphabetical order.")
        # for i in range(zones_count):
        #     print(i, zones[i].get_attribute("value"))
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        sleep(0.5)
print("paragraph 2")
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
geo_zones_count = len(driver.find_elements_by_css_selector("table.dataTable a:not([title=Edit])"))
print("Geo zones count", geo_zones_count)
for i in range(geo_zones_count):
    #enter into Geozone
    driver.find_element_by_css_selector("table.dataTable tr.row:nth-child("+str(i+2)+") a:not([title = Edit])").click()
    # find all zones in this geozone
    zones_list = driver.find_elements_by_css_selector("table.dataTable select[name *= zone_code] option[selected = selected]")
    print("zones count", len(zones_list))
    if all(zones_list[i].get_attribute("label") <= zones_list[i+1].get_attribute("label") for i in range(len(zones_list)-1)):
        print("paragraph 2 Geo Zones are in alphabetical order.")
    else:
        print("paragraph 2 Geo Zones are NOT in alphabetical order.")
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
# table.dataTable select[name *= zone_code] option[selected = selected] label
driver.quit()