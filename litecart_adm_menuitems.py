from litecart_adm_login import lcadm_login
import time

driver = lcadm_login()
arr1 = driver.find_elements_by_css_selector("li#app->a")
for itemno in range(len(arr1)):
    print("меню верхнего уровня номер: "+str(itemno+1))
    driver.find_element_by_xpath("(//li[@id='app-'])["+str(itemno+1)+"]").click()
    arr2 = driver.find_element_by_xpath("(//li[@id='app-'])["+str(itemno+1)+"]").find_elements_by_css_selector("li")
    print("кол-во подменю: "+str(len(arr2)))
    # print(arr2)
driver.quit()