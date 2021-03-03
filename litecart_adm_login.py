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
    driver = lcadm_login()
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()