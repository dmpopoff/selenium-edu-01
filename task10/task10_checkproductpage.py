from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/litecart/en/")
sleep(1)
# а) на главной странице и на странице товара совпадает текст названия товара
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