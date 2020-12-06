import yaml
import time
from selenium import webdriver

# get account config
with open(r'./config.yml') as file:
    documents = yaml.full_load(file)

    for key, value in documents.items():
        if key == 'id':
            id = value
        elif key == 'pw':
            pw = value


def login(id, pw, driver):
    # goto login page
    driver.get('https://nid.naver.com/nidlogin.login')
    time.sleep(1)

    # input id, password
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    time.sleep(1)
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    time.sleep(1)

    # click login button
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(1)

def find_latest_blog(keyword, driver):
    search_keywords = 'https://search.naver.com/search.naver?where=blog&sm=tab_opt&query=' + keyword + '&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Aall'
    driver.get(search_keywords)
    time.sleep(1)


driver = webdriver.Chrome('./chromedriver')
login(id, pw, driver)
find_latest_blog('키보드 리뷰', driver)



