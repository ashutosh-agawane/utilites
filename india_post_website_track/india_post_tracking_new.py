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


def Driver(url):
    global search_bar, lable, driver, image, add_text
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        options=options, executable_path=r'./chromedriver')
    driver.maximize_window()

    driver.get(url)

    search_bar = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_ucNewLegacyControl_txtOrignlPgTranNo")
    lable = driver.find_elements_by_xpath(
        '/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')[0].text
    image = driver.find_elements_by_tag_name("img")

    add_text = driver.find_element_by_xpath(
        '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_txtCaptcha"]')


def import_data():
    global awbno, db
    client = MongoClient()
    db = client["vikrant"]
    # print(db)
    input_data = db.input_sent.find().limit(5)
    # print(input_data)
    for i in input_data:
        try:

            awbno = i["Post_Barcode"]
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
                Driver(
                    "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
        except Exception as e:
            print(e)
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
                add = int(get_num[0]) + int(get_num[1])
                add_text.send_keys(add)
                submit = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
                print(add)
                extract_data()
                # awbno = driver.find_element_by_xpath(
                # "/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/strong/span").text
                # print(awbno)

            elif j in "-":
                sub = int(get_num[0]) - int(get_num[1])
                add_text.send_keys(sub)
                submit = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
                print(sub)
                extract_data()


def Alphanumerric_captcha():
    global result
    # print(result)
    image_conversion()
    for i in result:
        remve_space = i.replace(" ", "")
        print(remve_space)
        add_text.send_keys(remve_space)
        submit = driver.find_element_by_xpath(
            '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        extract_data()


def extract_data():
    ob = Screenshot_Clipping.Screenshot()

    sleep_time = [40, 50, 60, 70, 100, 105]
    s = random.choice(sleep_time)
    try:
        element_present = EC.presence_of_element_located(
            (By.ID, 'ctl00_PlaceHolderMain_ucNewLegacyControl_lblMailArticleDtlsOER'))
        WebDriverWait(driver, s).until(
            element_present)
        print(s)
    except TimeoutException:
        print("Timed out waiting for page to load")

    loading_page = driver.page_source
    # print(loading_page)

    # soup4 = BeautifulSoup(loading_page, 'lxml')
    # table = soup4.find("table", {
    #     "id": "ctl00_PlaceHolderMain_ucNewLegacyControl_gvTrckMailArticleEvntOER"})
    # # print(table)
    # table_rows = table.find_all("tr", {"center"})
    # print(table_rows)
    # for tr in table_rows:
    #     # td = tr.find_all("td")
    #     # th = tr.find_all("th")
    #     # row1 = [i.text for i in th]
    #     # row2 = [i.text for i in td]
    #     # li = [row1, row2]
    #     print(tr)
    # new_url = driver.current_url
    # print(new_url)
    df = pd.read_html(loading_page)[1]
    # d = df.to_dict()
    # insert = db.data.insert_one(d)
    print(df)


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
            extract_data()
        elif "Second" in lable:
            second_number = remve_space[1]
            add_text.send_keys(second_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            extract_data()
        elif "Third" in lable:
            third_number = remve_space[2]
            add_text.send_keys(third_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            extract_data()
        elif "Fourth" in lable:
            fourth_number = remve_space[3]
            add_text.send_keys(fourth_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
            extract_data()
        elif "Fifth" in lable:
            fifth_number = remve_space[4]
            add_text.send_keys(fifth_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
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
    Driver("https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
    import_data()
    # main()
