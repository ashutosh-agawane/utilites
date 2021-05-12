from datetime import datetime
import pdfkit
import codecs
import pandas as pd
import random
from http import client
from logging import error
from numpy.core.arrayprint import printoptions
from numpy.lib.type_check import imag
from pandas.core.frame import DataFrame
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import base64
# from six import StringIO
from PIL import Image, ImageEnhance
from pyvirtualdisplay import Display
import cv2
import numpy as np
import pytesseract
import cv2
import numpy as np
import imutils
import pytesseract
from Screenshot import Screenshot_Clipping
from pyhtml2pdf import converter
import cv2
import os
from bs4 import BeautifulSoup

from easyocr import Reader
import easyocr
import cv2
from matplotlib import pyplot as pit
import numpy as np
import re
from bs4 import BeautifulSoup as bs
import urllib.request
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymongo import MongoClient
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ob = Screenshot_Clipping.Screenshot()
today = datetime.today()
mydate = today.strftime("%Y/%m/%d")
now = datetime.now()


def Driver(url):
    global search_bar, lable, driver, image, add_text, error_lable
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.headless = True

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

    error_lable = driver.find_element_by_xpath(
        '/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/small/span[1]').text


def import_data():
    global awbno, db, i, mongo_id
    client = MongoClient()
    db = client["vikrant"]
    # print(db)
    # EM698867672IN
    # input_data = ["EM698867669IN", "EM777606405IN", "EM777630673IN",
    #               "EM777630660IN", "EM699081499IN", "EM699081600IN", "EM777790587IN"]
    input_data = db.test.find({"india_post": "100"})
    # input_data = db.test.find({"india_post": {"$exists": False}})
    # input_data = db.test1.find()

    # print(input_data)
    for i in input_data:
        try:
            mongo_id = i['_id']
            awbno = i["Post_Barcode"]
            # awbno = i["POD NO"]
            print(awbno)
            search_bar.send_keys(awbno)
        # driver.close()
            if lable == "Evaluate the Expression":
                Maths_captcha()
                # print("Current session is {}".format(driver.session_id))
                driver.quit()
                Driver(
                    "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
                # continue

            elif lable == "Enter characters as displayed in image":
                Alphanumerric_captcha()
                # print("Current session is {}".format(driver.session_id))
                driver.quit()
                Driver(
                    "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
                # continue
            else:
                finding_index_number_captcha()
                # print("Current session is {}".format(driver.session_id))
                driver.quit()
                # continue
                Driver(
                    "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
        except Exception as e:
            print(e)
            # raise (e)
            update = db.test.update_one({"_id": mongo_id}, {
                "$set": {"india_post": "100", "updatedAt": mydate}}, upsert=True)
            continue


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
            # gray = cv2.bitwise_not(gray)
            ret, thresh = cv2.threshold(gray, 150, 255, 1)
            # Get countours
            contours, h = cv2.findContours(thresh, 1, 2)
            # Draw
            cv2.drawContours(im_read, contours, -1, (0, 0, 0), 2)
            # cv2.imshow('Contours', image)
            # cv2.waitKey(0)
            cv2.imwrite("image_converted.jpg", im_read)
            reader = Reader(['en'], gpu=False)

            result = reader.readtext("image_converted.jpg",
                                     detail=0, paragraph=True)


def Maths_captcha():
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
                # add = int(get_num[0]) + int(get_num[1])
                cap1 = str(input("Enter the catcha :"))
                add_text.send_keys(cap1)
                submit = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
                print(error_lable)
                # print(add)
                # if error_lable
                # if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                #     driver.close()
                #     continue
                # else:
                extract_data()

                # awbno = driver.find_element_by_xpath(
                # "/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/strong/span").text
                # print(awbno)

            elif j in "-":
                # sub = int(get_num[0]) - int(get_num[1])
                cap1 = str(input("Enter the catcha :"))
                add_text.send_keys(cap1)
                submit = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
                print(error_lable)

                # print(sub)
                # if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                #     driver.close()
                #     continue
                # else:
                extract_data()


def Alphanumerric_captcha():
    global result
    # print(result)
    image_conversion()
    for i in result:
        # remve_space = i.replace(" ", "")
        # print(remve_space)
        cap1 = str(input("Enter the catcha :"))

        add_text.send_keys(cap1)
        submit = driver.find_element_by_xpath(
            '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        print(error_lable)
        # if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
        #     driver.close()
        #     continue
        # else:
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
    img_url = ob.full_Screenshot(
        driver, save_path=r'.', image_name='sceenshot.png')
    image1 = Image.open(r'sceenshot.png')
    im1 = image1.convert('RGB')
    im1.save(
        r'E:\python\data\india_post_website_track\pdfs\{}.pdf'.format(awbno))
    # except TimeoutException:
    #     print("Timed out waiting for page to load")

    loading_page = driver.page_source
    soup4 = BeautifulSoup(loading_page, 'lxml')
    table = soup4.find("table", {
        "id": "ctl00_PlaceHolderMain_ucNewLegacyControl_gvTrckMailArticleEvntOER"})
    # # print(table)
    table_rows = table.tbody.find_all("tr")
    # # print(table_rows[0])
    # th = [th.text.replace('\n', ' ').strip()
    #       for th in table_rows[0].find_all("th")]
    # for td in table_rows[0].find_all("th"):
    td = [td.text.replace('\n', ' ').strip()
          for td in table_rows[1].find_all("td")]
    #     headings.append(td.text.replace('\n', ' ').strip())
    # td = tr.find_all("td")
    # # print(th)
    # # print(td)

    # # # th = tr.find_all("th")
    # # # row1 = [i.text for i in th]
    # # row2 = [i.text for i in td]
    # # # # li = [row1, row2]
    # # print(row2)
    # #     for k in row2:
    # #         print(k[0])
    # # new_url = driver.current_url
    # # print(new_url)
    # # df = pd.read_html(loading_page)[1]
    # # # f = df.drop(index=[0])
    # # d = df.to_json()
    my_dist = {
        "awbno": awbno,
        "date": td[0],
        "time": td[1],
        "office": td[2],
        "status": td[3],
        "created_at": mydate
    }
    # print(my_dist)
    # df = pd.DataFrame(data=my_dist)
    # df = (df.T)
    # df.to_excel('dict1.xlsx')
    # # p = df.style.hide_index()
    insert = db.test_data.insert_one(my_dist)
    update = db.test.update_one({"_id": mongo_id}, {
        "$set": {"india_post": "200", "updatedAt": mydate}}, upsert=True)

    print("done")


def finding_index_number_captcha():
    global result
    image_conversion()
    for i in result:
        remve_space = i.replace(" ", "")
        # print(remve_space[0])
        # print(remve_space[1])
        # print(remve_space[2])
        # print(remve_space[3])
        # print(remve_space[4])
        if "First" in lable:
            first_number = remve_space[0]
            add_text.send_keys(first_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                driver.close()
                continue
            else:
                extract_data()
        elif "Second" in lable:
            second_number = remve_space[1]
            add_text.send_keys(second_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                driver.close()
                continue
            else:
                extract_data()

        elif "Third" in lable:
            third_number = remve_space[2]
            add_text.send_keys(third_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                driver.close()
                continue
            else:
                extract_data()

        elif "Fourth" in lable:
            fourth_number = remve_space[3]
            add_text.send_keys(fourth_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                driver.close()
                continue
            else:
                extract_data()

        elif "Fifth" in lable:
            fifth_number = remve_space[4]
            add_text.send_keys(fifth_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            if driver.find_element_by_xpath("/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]"):
                driver.close()
                continue
            else:
                extract_data()

# def main():
#     search_bar.send_keys(awbno)
#     # driver.close()
#     if lable == "Evaluate the Expression":
#         Maths_captcha()
#         driver.close()


#     elif lable == "Enter characters as displayed in image":
#         Alphanumerric_captcha()
#         driver.close()
#     else:
#         finding_index_number_captcha()
#         driver.close()
if __name__ == "__main__":
    begin = time.time()
    Driver("https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
    import_data()
    # main()
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")
