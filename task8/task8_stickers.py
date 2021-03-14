from selenium import webdriver

options = webdriver.ChromeOptions();
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")

product_carts = driver.find_elements_by_css_selector("li.product")
print(len(product_carts))