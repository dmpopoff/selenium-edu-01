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
    driver.find_element_by_name("password").send_keys("admin123")
    driver.find_element_by_name("login").click()
    return driver

def main():
    #login
    driver = lcadm_login()
    time.sleep(1)
    # click Catalog
    driver.find_element_by_css_selector("li#app-:nth-child(2)").click()
    time.sleep(1)
    #get initial product count
    product_count1 = len(driver.find_elements_by_css_selector("table.dataTable tr.row"))
    # click add product a.button:nth-child(2)
    driver.find_element_by_css_selector("a.button:nth-child(2)").click()
    # fill in tab General
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=radio][value='1']").click()
    driver.find_element_by_css_selector("input[name^=name]").send_keys("product1")
    driver.find_element_by_css_selector("input[name^=new_images]").send_keys(r'C:\python\1.jpg')
    time.sleep(3)
    # fill in tab Information
    driver.find_element_by_css_selector("ul.index a[href='#tab-information']").click()
    driver.find_element_by_css_selector("input[name=keywords]").send_keys("product1")
    time.sleep(3)
    # fill in tab Prices
    driver.find_element_by_css_selector("ul.index a[href='#tab-prices']").click()
    driver.find_element_by_css_selector("input[name=purchase_price]").clear()
    driver.find_element_by_css_selector("input[name=purchase_price]").send_keys("24")
    # click Save
    driver.find_element_by_css_selector("button[name=save]").click()
    # check new product in admin panel
    product_count2 = len(driver.find_elements_by_css_selector("table.dataTable tr.row"))
    print(product_count1, product_count2)
    if product_count1<product_count2:
        print("новый продукт добавлен")
    else:
        print("новый продукт НЕ добавлен")
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()