import json
import init

driver, logger = init.initConfig(True)

# record the start
logger.info("start init_baidu.py")

# init some config.json
config = {}
# load config file
with open("config.json", 'r') as f:
    config = json.load(f)
# homepage & add cookie
homepage = config["baidu"]["urls"]["homepage"]
# must get the site beofre add cookie
driver.get(homepage)
for c in config["baidu"]["cookie"]:
    driver.add_cookie(cookie_dict=c)

target = config["baidu"]["urls"]["target"]

passwd = config["baidu"]["xpath"]["passwd"]

passwd_enter = config["baidu"]["xpath"]["passwd_enter"]

logger.info("init_baidu.py end")
