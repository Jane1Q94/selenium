from selenium import webdriver
import time
import csv


def write_result(list,filename="result.csv"):
    """
    write result to csv file
    :param list: list contains result of one row.
    :return:
    """
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(list)

def nextpage(driver, path_id, xpath, sum):
    """
    go to the next page
    :param driver: browser instance
    :param xpath: element's xpath
    :return: None next page
    """
    print(sum)
    ul(driver,xpath)
    element = driver.find_element_by_id(path_id)
    element_next = element.find_elements_by_xpath("a")[-2]
    if "shark-pager-disable" in str(element_next.get_attribute("class")) or sum==10:
        return
    else:
        sum += 1
        element_next.click()
        try:
            #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "jumppage")))
            time.sleep(2)
            nextpage(driver, path_id, xpath, sum)
        except Exception as e:
            print("error" + str(e))


def ul(driver, xpath):
    lis = driver.find_elements_by_xpath(xpath)
    for li in lis:
        try:
            element_a = li.find_element_by_tag_name("a")
            li = [element_a.get_attribute("title"), element_a.get_attribute("href")]
            write_result(li)

        except Exception as e:
            print("don't have the element")
            break
    print('*******************************')

def main():
    url = "http://www.douyu.com/directory/all"
    driver = webdriver.Chrome()
    driver.get(url)
    xpath_ul = "//ul[@id='live-list-contentbox']/li"
    page_id = "J-pager"
    nextpage(driver,page_id,xpath_ul,1)


main()




