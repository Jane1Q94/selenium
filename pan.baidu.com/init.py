from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging.config

def __loggingConfig(loggerName):
    """
    private function to set logger

    :param logger:
    :return:
    """
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(loggerName)





def initConfig(headless=False):
    """
    set the driver mode(headless or not);
    set the logging;

    :param headless:
    :return:
    """
    loggerName = "cf"
    logger = __loggingConfig(loggerName)


    if headless:
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_option)

    else:
        driver = webdriver.Chrome()

    return (driver, logger)


logging.info("end init.py")
