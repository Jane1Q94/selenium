from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger("BaiDuTieBa")
logger.setLevel(logging.DEBUG)

driver = webdriver.Chrome()


def log(logger):
    fh = logging.FileHandler("tieba.log", mode='a', encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fmt = "%(asctime)15s %(lineno)15d %(message)15s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formater = logging.Formatter(fmt, datefmt)
    fh.setFormatter(formater)
    logger.addHandler(fh)

def wait(xpath, id=None, presence=0):
    """

    :param driver: browser instance
    :param xpath: locate element by xpath default
    :param id: locate element by id by setting id value equal 1
    :param click: wait untile element is clickble
    :param presence: wait untile element is presence
    :return: element
    """
    wait = WebDriverWait(driver, 4, 0.5)
    if id is None:
        if presence == 0:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        else:
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    else:
        if presence == 0:
            element = wait.until(EC.element_to_be_clickable((By.ID, id)))
        else:
            element = wait.until(EC.presence_of_element_located((By.ID, id)))

    return element

def go_page_by_xpath(xpath):
    element = wait(xpath)
    element.click()

def login():
    driver.get("http://tieba.baidu.com")
    time.sleep(2)
    tieba_login_xpath = "//*[@id='com_userbar']/ul/li[4]/div/a"
    tieba_login_vertify = "//*[@id='TANGRAM__PSP_10__footerULoginBtn']"
    go_page_by_xpath(tieba_login_xpath)
    go_page_by_xpath(tieba_login_vertify)
    user_xpath = "//*[@id='TANGRAM__PSP_10__userName']"
    passwd_xpath = "//*[@id='TANGRAM__PSP_10__password']"
    submit_xpath = "//*[@id='TANGRAM__PSP_10__submit']"

    user = driver.find_element_by_xpath(user_xpath)
    passwd = driver.find_element_by_xpath(passwd_xpath)
    submit = driver.find_element_by_xpath(submit_xpath)
    time.sleep(2)
    user.send_keys("15618884895")
    time.sleep(2)
    passwd.send_keys("chinawin7890")
    time.sleep(2)
    submit.click()
    time.sleep(2)

def search_tieba(search_input, vertify_input, name):
    time.sleep(1)
    element_search = wait(search_input, presence=1)
    element_search.send_keys(name)

    element_vertify = wait(vertify_input)
    element_vertify.click()

def like_tieba(xpath):
    time.sleep(1)
    element_like = wait(xpath)
    element_like.click()
    driver.refresh()

def readmessage(title=0, content=0):
    time.sleep(1)
    with open("tieba.txt", 'r') as f:
        tiezi = f.readlines()
        if title == 1 and content == 0:
            return str(tiezi[0])

        elif title == 0 and content == 1:
            return "".join(tiezi[1:])
        else:
            return

def write_message(xpathWriteButton, xpath_title, xpath_message, xpath_vertify):
    time.sleep(1)
    element_write_button = wait(xpathWriteButton)
    element_write_button.click()
    element_title = wait(xpath_title, presence=1)
    element_message = wait(xpath_message, presence=1)
    element_vertify = wait(xpath_vertify)
    message = readmessage(title=1)
    content = readmessage(content=1)
    element_title.send_keys(message)
    element_message.send_keys(content)
    element_vertify.click()

def read_tieba_name():
    with open("tieba_name",'r') as f:
        return f.readlines()

def write_message_all(search_name):
     #search tieba
    search_input = "//*[@id='wd1']"
    vertify_input = "//*[@id='tb_header_search_form']/span[1]/a"
    search_tieba(search_input, vertify_input, search_name)
     #write message
    message = "/html/body/ul/li[2]/a"
    title = "//*[@id='tb_rich_poster']/div[3]/div[1]/div[2]/input"
    content = "//*[@id='ueditor_replace']"
    vertify = "//*[@id='tb_rich_poster']/div[3]/div[5]/div/button[1]"
    write_message(message, title, content, vertify)
    driver.get("http://tieba.baidu.com")
    time.sleep(2)

def main():


    like = "//*[@id='j_head_focus_btn']"
    #like_tieba(driver, like)
    login()
    #tieba_name = read_tieba_name()
    #for name in tieba_name:
        # write_message_all(name)
    # time.sleep(2)


main()

log(logger)

logger.debug("test")

print(driver.get_cookies())
