from selenium import webdriver

options = webdriver.ChromeOptions();
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")

product_carts = driver.find_elements_by_css_selector("li.product")
for sticker in range(len(product_carts)):
    if len(product_carts[sticker].find_elements_by_css_selector("div.sticker"))>0:
        print("sticker is here!")
    else:
        print("where is no sticker here(((")
driver.quit()