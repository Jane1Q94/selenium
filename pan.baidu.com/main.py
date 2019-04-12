import json
import time
import init
import init_baidu

#init config contains driver and logging
driver, logger = init.initConfig(True)

logger.info("get target site(%s)" % init_baidu.target)
# get target site
driver.get(init_baidu.target)

# main: save content
# get the password element and enter the password
logger.info("get password element and input password")
passwd_element = driver.find_element_by_xpath(init_baidu.passwd).send_keys("1234")
time.sleep(2)

# get the password enter element.
get_element = driver.find_element_by_xpath(init_baidu.passwd_enter).click()
time.sleep(2)







