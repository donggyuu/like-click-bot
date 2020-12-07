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
        elif key == 'keyword':
            keyword = value


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
    try:
        search_keywords = 'https://search.naver.com/search.naver?where=blog&sm=tab_opt&query=' + keyword + '&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Aall'
        driver.get(search_keywords)
        time.sleep(2)

        targetBlog = driver.find_element_by_class_name("api_txt_lines") # target블로그 선택
        driver.get(targetBlog.get_attribute('href')) # target블로그를 현재창에서 열기(새창을 열면 미로그인상태로 인식됨)
        time.sleep(5) # 이미지가 많으면 페이지 로딩시간이 길 수 있으니 5초 정도 여유를 줌

    except Exception as e:
        print("[ERROR] cannot get latest blog:", e.args)


def clickLikeButton(driver):

    try:
        # 네이버 블로그는 전체적으로 iframe으로 감싸져 있기에 처리해줌
        mainFrame= driver.find_element_by_id("mainFrame")
        time.sleep(1)
        driver.switch_to.frame(mainFrame)

        # click like button
        try:
            driver.find_element_by_class_name('u_likeit_list_btn').click()
            time.sleep(4)
        except Exception as e:
            # pass if button not exist
            # 좋아요 버튼이 없으면 패스
            print("[WARN] cannot click an like-button:", e.args)

    except Exception as e:
        print("[ERROR] cannot click an like-button:", e.args)


# ---------------------------------------------
# headless option
# ---------------------------------------------
options = webdriver.ChromeOptions()
options.add_argument('headless') # 브라우저 창 안 띄우겠다
options.add_argument('window-size=1920x1080') # 보통의 FHD화면을 가정
options.add_argument("disable-gpu") # or options.add_argument("--disable-gpu")
# headless탐지 방지를 위해 UA를 임의로 설정
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# ---------------------------------------------
# execution
# ---------------------------------------------
driver = webdriver.Chrome('./chromedriver', options=options)
login(id, pw, driver)
getLatestBlog(keyword, driver)
clickLikeButton(driver)

driver.quit()