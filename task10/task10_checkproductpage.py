from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")
sleep(1)
# а) на главной странице и на странице товара совпадает текст названия товара
prod_name_main = driver.find_element_by_css_selector("div#box-campaigns div.name").get_attribute("innerText")
price_regular_main = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").get_attribute("innerText")
price_regular_main_isgrey = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("color")
price_regular_main_iscrossedout = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("text-decoration-line")
price_regular_main_size = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").get_attribute("innerText")
price_promo_main = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").get_attribute("innerText")
price_promo_main_isred = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").value_of_css_property("color")
price_promo_main_isbold = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").value_of_css_property("font-weight")
price_promo_main_size = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").get_attribute("innerText")
# price_promo_main_isbigger = 
print("prod_name_main", prod_name_main, 
"\nprice_regular_main", price_regular_main,  
"\nprice_regular_main_isgrey", price_regular_main_isgrey,
"\nprice_regular_main_iscrossedout", price_regular_main_iscrossedout,  
"\nprice_regular_main_size", price_regular_main_size,  
"\nprice_promo_main", price_promo_main,  
"\nprice_promo_main_isred", price_promo_main_isred, 
"\nprice_promo_main_isbold", price_promo_main_isbold, 
"\nprice_promo_main_size", price_promo_main_size)
# б) на главной странице и на странице товара совпадают цены (обычная и акционная)
# в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
# г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
# (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
# д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
# названия товара div#box-campaigns div.name innerText
# div#box-product h1.title
# обычная цена div#box-campaigns s.regular-price innerText
# div#box-product s.regular-price
# акционная div#box-campaigns strong.campaign-price innerText
# div#box-product strong.campaign-price
driver.quit()