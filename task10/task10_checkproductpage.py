from selenium import webdriver
from time import sleep
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")
sleep(1)

prod_name_main = driver.find_element_by_css_selector("div#box-campaigns div.name").get_attribute("innerText")
price_regular_main = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").get_attribute("innerText")
price_regular_main_isgrey = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("color")
price_regular_main_iscrossedout = driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("text-decoration-line")
price_regular_main_size = float(driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("font-size").removesuffix('px'))
price_promo_main = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").get_attribute("innerText")
price_promo_main_isred = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").value_of_css_property("color")
price_promo_main_isbold = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price").value_of_css_property("font-weight")
price_promo_main_size = float(driver.find_element_by_css_selector("div#box-campaigns s.regular-price").value_of_css_property("font-size").removesuffix('px'))
# print("type", type(price_promo_main_size))
# price_promo_main_isbigger = 
# print("Значения на главнойЖ")
# print("prod_name_main", prod_name_main, 
# "\nprice_regular_main", price_regular_main,  
# "\nprice_regular_main_isgrey", price_regular_main_isgrey,
# "\nprice_regular_main_iscrossedout", price_regular_main_iscrossedout,  
# "\nprice_regular_main_size", price_regular_main_size.removesuffix('px'),  
# "\nprice_promo_main", price_promo_main,  
# "\nprice_promo_main_isred", price_promo_main_isred, 
# "\nprice_promo_main_isbold", price_promo_main_isbold, 
# "\nprice_promo_main_size", price_promo_main_size.removesuffix('px'))
driver.find_element_by_css_selector("div#box-campaigns a").click()

prod_name_prod = driver.find_element_by_css_selector("h1").get_attribute("innerText")
price_regular_prod = driver.find_element_by_css_selector("s.regular-price").get_attribute("innerText")
price_regular_prod_isgrey = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("color")
price_regular_prod_iscrossedout = driver.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-line")
price_regular_prod_size = float(driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-size").removesuffix('px'))
price_promo_prod = driver.find_element_by_css_selector("strong.campaign-price").get_attribute("innerText")
price_promo_prod_isred = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("color")
price_promo_prod_isbold = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
price_promo_prod_size = float(driver.find_element_by_css_selector("s.regular-price").value_of_css_property("font-size").removesuffix('px'))
# print("значения на странице продукта: ")
# print("prod_name_prod", prod_name_prod, 
# "\nprice_regular_prod", price_regular_prod,  
# "\nprice_regular_prod_isgrey", price_regular_prod_isgrey,
# "\nprice_regular_prod_iscrossedout", price_regular_prod_iscrossedout,  
# "\nprice_regular_prod_size", price_regular_prod_size.removesuffix('px'),  
# "\nprice_promo_prod", price_promo_prod,  
# "\nprice_promo_prod_isred", price_promo_prod_isred, 
# "\nprice_promo_prod_isbold", price_promo_prod_isbold, 
# "\nprice_promo_prod_size", price_promo_prod_size.removesuffix('px'))
# а) на главной странице и на странице товара совпадает текст названия товара
if prod_name_main == prod_name_prod:
    print("названия товаров на главной и в карточке совпадают")
else:
    print("названия товаров на главной и в карточке НЕ совпадают")
# б) на главной странице и на странице товара совпадают цены (обычная и акционная)
if (price_regular_main == price_regular_prod) and (price_promo_main == price_promo_prod):
    print("цены акционная и обычная на главной и в карточке совпадают")
else:
    print("цены товаров на главной и в карточке отличаются")
# в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
regexp1 = re.compile('^rgba\(\d+,\s(\d{1,3}),\s(\d{1,3}),\s(\d{1})')
msg_main = regexp1.match(price_regular_main_isgrey)
msg_prod = regexp1.match(price_regular_prod_isgrey)
# print("groups", msg_main.groups())
if (price_regular_main_iscrossedout == "line-through") and (price_regular_prod_iscrossedout == "line-through") and (msg_main.group(1) == msg_main.group(2)) and (msg_prod.group(1) == msg_prod.group(2)) :
    print("обычная цена зачёркнутая и серая")
else:
    print("обычная цена НЕ (зачёркнутая и серая)")
# г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
msg_main = regexp1.match(price_promo_main_isred)
msg_prod = regexp1.match(price_promo_prod_isred)
# print("msg_main.group(1)", msg_main.group(1), "msg_main.group(2)", msg_main.group(2))
# print("groups", msg_main.groups())
if (price_promo_main_isbold == "700") and (price_promo_prod_isbold == "700") and msg_main.group(1) == '0' and msg_main.group(2) == '0' and msg_prod.group(1) == '0' and msg_prod.group(2) == '0' :
    print("акционная цена жирная и красная")
else:
    print("акционная цена НЕ (жирная и красная)")
# (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
# д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
if (price_regular_main_size <= price_promo_main_size) and (price_regular_prod_size <= price_promo_prod_size):
    print("акционная цена крупнее, чем обычная")
else:
    print("акционная цена НЕ крупнее, чем обычная")
driver.quit()