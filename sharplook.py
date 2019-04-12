from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

def downloadPic(driver, elem_pic):
    """

    :param driver:
    :param xpath:
    :return:
    """
    downAction = ActionChains(driver).move_to_element(elem_pic)
    downAction.context_click(elem_pic)
    downAction.send_keys(Keys.ENTER)
    downAction.perform()




def check(driver, xpath):
    """ get the element until found it.

    :param driver:  instance of browser
    :param xpath: the xpath of element
    :return: elem instance
    """
    try:
        elem = driver.find_element_by_xpath(xpath)
        return elem

    except:
        time.sleep(1)
        return check(driver, xpath)


def login(elem_login, elem_passwd, elem_submit):
    """ login the webpage

    :param driver:
    :return:
    """
    elem_login.clear()

    elem_passwd.clear()

    elem_login.send_keys("admin")

    elem_passwd.send_keys("chinawin")

    elem_submit.click()

def main():
    """

    :return:
    """
    try:
        driver = webdriver.Chrome()

        driver.get("http://192.168.21.198")

        elem_login = check(driver, "/html/body/main-container/right-view/ui-view/page-login/div[2]/form/input[1]")

        elem_passwd = check(driver, "/html/body/main-container/right-view/ui-view/page-login/div[2]/form/input[2]")

        elem_submit = check(driver, "/html/body/main-container/right-view/ui-view/page-login/div[2]/form/button")

        login(elem_login, elem_passwd, elem_submit)

        elem_pic = check(driver, "/html/body/main-container/right-view/ui-view/page-overview/dashboard-grid/div/ul/li[2]/dashboard-panel/div/div[2]/report-panel/div/div/area-chart/ng-echarts/div[1]")

        downloadPic(driver, elem_pic)

        time.sleep(2)

    except Exception as e:
        print(e)

    finally:
        driver.close()

if __name__ == "__main__":
    main()
