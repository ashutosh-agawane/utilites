import random
import re
import time
import urllib.request
from datetime import datetime
from logging import error
import cv2
from bs4 import BeautifulSoup
from easyocr import Reader
from numpy.core.arrayprint import printoptions
from numpy.lib.type_check import imag
from PIL import Image, ImageEnhance
from pymongo import MongoClient
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ob = Screenshot_Clipping.Screenshot()
today = datetime.today()
mydate = today.strftime("%Y/%m/%d")
now = datetime.now()
url = "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx"


def initial():
    global search_bar, lable, driver, image, add_text, error_lable, btn_click
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        options=options, executable_path=r'./chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)

    search_bar = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_ucNewLegacyControl_txtOrignlPgTranNo")
    lable = driver.find_elements_by_xpath(
        '/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')[0].text
    image = driver.find_elements_by_tag_name("img")

    add_text = driver.find_element_by_xpath(
        '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_txtCaptcha"]')

    btn_click = driver.find_element_by_xpath(
        '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]')


def import_data():
    global awbno, db, i, mongo_id
    client = MongoClient()
    db = client["vikrant"]
    input_data = db.test.find({"india_post": "100"})
    for i in input_data:
        try:
            mongo_id = i['_id']
            awbno = i["Post_Barcode"]
            print(awbno)
            search_bar.send_keys(awbno)
            if lable == "Evaluate the Expression":
                maths_captcha()
                driver.quit()
                initial()
            elif lable == "Enter characters as displayed in image":
                alpha_num_captcha()
                driver.quit()
                initial()
            else:
                finding_index_number_captcha()
                driver.quit()
                initial()
        except Exception as e:
            print(e)
            db.test.update_one({"_id": mongo_id}, {
                "$set": {"india_post": "100", "updatedAt": mydate}}, upsert=True)
            driver.quit()
            initial()


def image_conversion():
    # pass
    global result
    for im in image:
        src = im.get_attribute("src")
        if src.endswith("="):
            print(src)
            urllib.request.urlretrieve(src, "captcha_jpg.jpg")
            im1 = Image.open('captcha_jpg.jpg')
            im1.save('cap_png.png')
            im_read = cv2.imread('cap_png.png')
            gray = cv2.cvtColor(im_read, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 150, 255, 1)
            contours, h = cv2.findContours(thresh, 1, 2)
            cv2.drawContours(im_read, contours, -1, (0, 0, 0), 2)
            cv2.imwrite("image_converted.jpg", im_read)
            reader = Reader(['en'], gpu=False)
            result = reader.readtext("image_converted.jpg",
                                     detail=0, paragraph=True)


def maths_captcha():
    global result
    image_conversion()
    for i in result:
        # print(i)
        get_num = re.findall('[0-9]+', str(i))
        # print(get_num)
        find_symbol = re.findall('[+-]', str(i))
        # print(find_symbol)
        for j in find_symbol:
            if j in "+":
                add = int(get_num[0]) + int(get_num[1])
                add_text.send_keys(add)
                btn_click.click()
                extract_data()

            elif j in "-":
                sub = int(get_num[0]) - int(get_num[1])
                add_text.send_keys(sub)
                btn_click.click()
                extract_data()


def alpha_num_captcha():
    global result
    # print(result)
    image_conversion()
    for i in result:
        remve_space = i.replace(" ", "")
        add_text.send_keys(remve_space)
        btn_click.click()
        extract_data()


def extract_data():
    sleep_time = [40, 50, 60, 70, 100, 125, 150, 200, 300, 400, 500]
    s = random.choice(sleep_time)
    # try:
    element_present = EC.presence_of_element_located(
        (By.ID, 'ctl00_PlaceHolderMain_ucNewLegacyControl_lblMailArticleDtlsOER'))
    WebDriverWait(driver, s).until(
        element_present)
    print(s)
    ob.full_Screenshot(
        driver, save_path=r'.', image_name='sceenshot.png')
    image1 = Image.open(r'sceenshot.png')
    im1 = image1.convert('RGB')
    im1.save(
        r'E:\python\data\india_post_website_track\pdfs\{}.pdf'.format(awbno))
    loading_page = driver.page_source
    soup4 = BeautifulSoup(loading_page, 'lxml')
    table = soup4.find("table", {
        "id": "ctl00_PlaceHolderMain_ucNewLegacyControl_gvTrckMailArticleEvntOER"})
    table_rows = table.tbody.find_all("tr")
    td = [td.text.replace('\n', ' ').strip()
          for td in table_rows[1].find_all("td")]

    my_dist = {
        "awbno": awbno,
        "date": td[0],
        "time": td[1],
        "office": td[2],
        "status": td[3],
        "created_at": mydate
    }

    db.test_data.insert_one(my_dist)
    db.test.update_one({"_id": mongo_id}, {
        "$set": {"india_post": "200", "updatedAt": mydate}}, upsert=True)
    print("done")


def finding_index_number_captcha():
    global result
    image_conversion()
    for i in result:
        remve_space = i.replace(" ", "")
        if "First" in lable:
            first_number = remve_space[0]
            add_text.send_keys(first_number)
            btn_click.c
        elif "Second" in lable:
            second_number = remve_space[1]
            add_text.send_keys(second_number)
            btn_click.click()
        elif "Third" in lable:
            third_number = remve_space[2]
            add_text.send_keys(third_number)
            btn_click.click()

        elif "Fourth" in lable:
            fourth_number = remve_space[3]
            add_text.send_keys(fourth_number)
            btn_click.click()

        elif "Fifth" in lable:
            fifth_number = remve_space[4]
            add_text.send_keys(fifth_number)
            btn_click.click()


if __name__ == "__main__":
    begin = time.time()
    initial()
    import_data()
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")
