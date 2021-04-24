import numpy as np
import cv2
import re
import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import urllib.request
from easyocr import Reader
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_all_images():
    """
    Returns all image URLs on a single `url`
    """
    im1 = Image.open('getCapchaImage (1).jpg')
    im1.save('getCapchaImage (1).png')

    image = cv2.imread('getCapchaImage (1).png')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.bitwise_not(gray)
    ret, thresh = cv2.threshold(gray, 150, 255, 1)
    # Get countours
    contours, h = cv2.findContours(thresh, 1, 2)
    # Draw
    cv2.drawContours(image, contours, -1, (0, 0, 0), 2)
    # cv2.imshow('Contours', image)
    # cv2.waitKey(0)
    cv2.imwrite("image1.jpg", image)
    reader = Reader(['en'], gpu=False)
    res = reader.readtext("image1.jpg", detail=0, paragraph=True)
    print(res)
    # for i in res:
    #     r = i.replace("€", "c")
    #     print(r)
    # get_num = re.findall('[0-9]+', str(i))
    # # print(get_num)
    # find_symbol = re.findall('[+-]', str(i))
    # # print(find_symbol)
    # for j in find_symbol:
    #     if j in "+":
    #         add = int(get_num[0]) + int(get_num[1])
    #         print(add)
    #         # print("yes")
    #     elif j in "-":
    #         sub = int(get_num[0]) - int(get_num[1])
    #         print(sub)
    # print(j)
    # options = webdriver.ChromeOptions()
    # # options.add_argument("--headless")
    # # options.headless = True
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # driver = webdriver.Chrome(
    #     options=options, executable_path=r'./chromedriver')

    # main = driver.get(url)

    # d = driver.find_elements_by_tag_name("img")
    # for i in d:

    #     src = i.get_attribute("src")
    #     if src.endswith("="):
    #         # print(src)
    #         urllib.request.urlretrieve(src, "cap.jpg")

    # beautiful soup
    # soup = bs(requests.get(url).content, "html.parser")
    # urls = []
    # for img in soup.find_all("img"):
    #     img_url = img.attrs.get("src")
    #     if img_url.startswith("."):
    #         # print(img_url)
    #         r = img_url.replace(
    #             "..", "https://www.indiapost.gov.in/_layouts/15")
    #         # print(r)
    #         urllib.request.urlretrieve(r, "cap.jpg")

    #         im1 = Image.open(r'cap.jpg')
    #         im1.save(r'cap.png')

    # convrt = pytesseract.image_to_string(r'cap.png')
    # print(convrt)

    # filename = "sample.jpg"

    # reader = Reader(['en'], gpu=False)

    # res = reader.readtext("cap.png", detail=0, paragraph=True)
    # print(res)
    # res = reader.readtext(filename, detail=0, paragraph=True)
    # for t in res:
    # print(t)
    # remvre_space = t.replace(" ", "")
    # print(remvre_space)
    # print(res)
    # print(x)

    #     if not img_url:
    #         # if img does not contain src attribute, just skip
    #         continue
    #         # make the URL absolute by joining domain with the URL that is just extracted
    #     img_url = urljoin(url, img_url)
    #     try:
    #         pos = img_url.index("?")
    #         img_url = img_url[:pos]
    #     except ValueError:
    #         pass
    #         # finally, if the url is valid
    #     if is_valid(img_url):
    #         urls.append(img_url)
    # return urls

    # main("https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx",
    #  "E:\python\data\india_post_website_track")
# get_all_images(
    # "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")
# E: \python\data\india_post_website_track
get_all_images()
