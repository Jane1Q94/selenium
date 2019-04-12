from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import argparse
import time


def writeTofile(str, filename="novel.txt"):
    with open(filename, 'a') as f:
        f.write(str)
        f.write("\n\n")


def log(logger):
    logger.setLevel(logging.DEBUG)
    fh = logging.StreamHandler()
    fh.setLevel(logging.DEBUG)
    fmt = "%(asctime)s %(lineno)d %(message)s"
    datefmt = "%H:%M:%s"
    formatter = logging.Formatter(fmt, datefmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)



def nextPage(driver, next_id, end_id, content_id, num):
    driver.set_window_size(1280, 800)
    logger.debug(num)
    chapter = "Chapter"
    content = chapter + str(num) + "\n" + driver.find_element_by_id(content_id).text
    writeTofile(content)
    time.sleep(2)
    next_element_div = driver.find_element_by_id(next_id)
    next_element = next_element_div.find_elements_by_xpath("a")[-1]
    href = str(next_element.get_attribute("href"))
    if end_id in href:
        return
    else:
        next_element.click()
        num += 1

        nextPage(driver, next_id, end_id, content_id,num)



def main():


    chrome_option = Options()
    chrome_option.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=chrome_option)


    driver.get("http://www.wutuxs.com/html/3/3740/2576260.html")

    content_id = "contents"
    next_id = "footlink"
    end_id = "index.html"

    nextPage(driver, next_id, end_id, content_id, 1)

logger_name = "novel"
logger = logging.getLogger(logger_name)
log(logger)
logger.debug("test")
main()