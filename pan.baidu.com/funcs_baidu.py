import init
import re

content = "集合链接: http://pan.baidu.com/s/1dDgxSid 提取码: 5tav，，，，，，集合链接: http://pan.baidu.com/s/1dDgxSid 提取码: 5tav，，，，，集合链接: http://pan.baidu.com/s/1dDgxSid 提取码: 5tav。。。。。。。jkjl，，，集合链接: http://pan.baidu.com/s/1dDgxSid"

url = re.compile(r'(http://pan.baidu.com\S+)')
passwd = re.compile(r'[密码|提取码]:\s+([\d|\w]{4})')

print(url.findall(content))
print(passwd.findall(content))


#_, logger = init.initConfig(True)

def search(driver):
    #logger.info("start search function")
    pass

def match():
    pass