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

def getLatestBlog(keyword, driver):
    search_keywords = 'https://search.naver.com/search.naver?where=blog&sm=tab_opt&query=' + keyword + '&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Aall'
    driver.get(search_keywords)

    # open a new page may takes some time
    # 이미지가 많으면 페이지 로딩시간이 길 수 있으니 5초 정도 여유를 줌
    time.sleep(5)
    
    # move to current page
    # 새롭게 연 블로그 페이지로 포인터 이동
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)


def clickLikeButton(driver):

    try:
        # 네이버 블로그는 전체적으로 iframe으로 감싸져 있기에 처리해줌
        mainFrame= driver.find_element_by_id("mainFrame")
        time.sleep(1)
        driver.switch_to.frame(mainFrame)

        # click like button
        try:
            driver.find_element_by_class_name('u_likeit_list_btn').click()
        except:
            # pass if button not exist
            # 좋아요 버튼이 없으면 패스
            print("[WARN] like-button not exist")

    except Exception as e:
        print("[ERROR] cannot click an like-button:", e.args)

# execution
driver = webdriver.Chrome('./chromedriver')
login(id, pw, driver)
getLatestBlog('키보드 리뷰', driver)
clickLikeButton(driver)



