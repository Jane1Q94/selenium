from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

form_elem = driver.find_element_by_xpath("//*[@id='form']")

options = form_elem.find_elements_by_xpath("//form/input")

for option in options:
    print(option.get_attribute("name"))

driver.close()



