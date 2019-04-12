from selenium import webdriver
import time

def get_cookie(cookie):
    return dict([c.split("=", 1) for c in cookie.split("; ")])


def add_cookie(driver, cookie):
    for key, value in cookie.items():
        # if key in ("BAIDUID", "BDUSS"):
        driver.add_cookie({"name":key, "value":value})

def go_page_by_id(driver, id):
    baidu_element = driver.find_element_by_id(id)
    tieba_element = baidu_element.find_elements_by_xpath("a")[4]
    tieba_element.click()
    time.sleep(2)


def go_page_by_xpath(driver, xpath):
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)


def login(driver, user_xpath, passwd_xpath, subimit_xpath):
    user = driver.find_element_by_xpath(user_xpath)
    passwd = driver.find_element_by_xpath(passwd_xpath)
    submit = driver.find_element_by_xpath(subimit_xpath)
    user.send_keys("15618884895")
    time.sleep(2)
    passwd.send_keys("chinawin")
    time.sleep(2)
    submit.click()
    time.sleep(2)





def main():
    driver = webdriver.Chrome()
    #cookie = "BAIDUID=1AC5C49D4F1550D055F95711DB455148:FG=1; BDUSS=tafnBqVkRwd1Flc3dZcmhIQk8yMzVSVX5kckRTN05icmluQjRvVXNHelQ4QjFjQVFBQUFBJCQAAAAAAAAAAAEAAACd93voSmFuMXE5NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANNj9lvTY~ZbNG"
    driver.get("https://tieba.baidu.com/")

    #cookie_dict = get_cookie(cookie)
    #add_cookie(driver, cookie_dict)

    #print(driver.get_cookies())

    #driver.get("https://tieba.baidu.com/")

    #print(driver.get_cookies())

    #time.sleep(4)

    tieba_xpath = "//*[@id='com_userbar']/ul/li[4]/div/a"
    tieba_login_xpath = "//*[@id='TANGRAM__PSP_10__footerULoginBtn']"
    go_page_by_xpath(driver, tieba_xpath)
    time.sleep(2)
    go_page_by_xpath(driver, tieba_login_xpath)
    time.sleep(2)
    user_xpath = "//*[@id='TANGRAM__PSP_10__userName']"
    passwd_xpath = "//*[@id='TANGRAM__PSP_10__password']"
    submit_xpaht = "//*[@id='TANGRAM__PSP_10__submit']"
    login(driver, user_xpath,passwd_xpath, submit_xpaht)
    time.sleep(100)


main()
