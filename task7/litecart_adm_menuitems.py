from litecart_adm_login import lcadm_login
import time

driver = lcadm_login()
arr1 = driver.find_elements_by_css_selector("li#app->a")
time.sleep(2)
for itemno in range(len(arr1)):
    print("меню верхнего уровня номер: "+str(itemno+1))
    xpath = "(//li[@id='app-'])["+str(itemno+1)+"]/a"
    time.sleep(0.5) # Chrome bug: cannot click to first menu entry. Alexey Barancev
    driver.find_element_by_xpath(xpath).click()
    arr2 = driver.find_element_by_xpath("(//li[@id='app-'])["+str(itemno+1)+"]").find_elements_by_css_selector("li")
    print("кол-во подменю: "+str(len(arr2)))
    headerH1 = driver.find_elements_by_css_selector("h1")
    if len(headerH1)>0:
        print("H1 is here")
    else:
        print("H1 is not here")
    for submenu in range(len(arr2)):
        print("     подменю номер: "+str(submenu+1))
        time.sleep(0.5) # Chrome bug: cannot click to first menu entry. Alexey Barancev
        topmenu = driver.find_element_by_xpath("(//li[@id='app-'])["+str(itemno+1)+"]")
        submenu_item = topmenu.find_element_by_xpath("(.//li)["+str(submenu+1)+"]")
        submenu_item.click()
        headerH1 = driver.find_elements_by_css_selector("h1")
        if len(headerH1)>0:
            print("     H1 is here")
        else:
            print("     H1 is not here")
driver.quit()