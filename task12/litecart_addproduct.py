from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time

def lcadm_login():
    options = webdriver.ChromeOptions();
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    return driver

def main():
    #login
    driver = lcadm_login()
    # click Catalog li#app-:nth-child(2)
    driver.find_element_by_css_selector("li#app-:nth-child(2)").click()
    time.sleep(1)
    # click add product a.button:nth-child(2)
    # fill in tab General 
    # fill in tab Information
    # fill in tab Prices
    # click Save
    # check new product in admin
    time.sleep(8)
    driver.quit()

if __name__ == "__main__":
    main()