from logging import error
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import base64
from io import StringIO, BytesIO
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

from captcha_solver import CaptchaSolver
from operator import itemgetter
import argparse
import cv2
import os

from easyocr import Reader
import easyocr
import cv2
from matplotlib import pyplot as pit
import numpy as np
import re
from bs4 import BeautifulSoup as bs
import urllib.request

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def drivers():
    global driver
    # driver = webdriver.Chrome('./chromedriver')

    # driver.get(
    # "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        options=options, executable_path=r'./chromedriver')

    main = driver.get(
        "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")


def search_awbno():
    global search_bar

    search_bar = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_ucNewLegacyControl_txtOrignlPgTranNo")

    search_bar.send_keys("EM698851482IN")


def lab():
    global lable, error_lable
    # lable = driver.find_element_by_class_name('required')
    # print(lable)
    lable = driver.find_elements_by_xpath(
        '/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/span/span')[0].text
    # print(lable)
    # error_lable = driver.find_elements_by_xpath(
    #     '/html/body/form/div[4]/div/div/div[5]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/small/span[1]').text


def solving_captcha():
    global lable, error_lable

    if lable == "Evaluate the Expression":
        print("express here")
        d = driver.find_elements_by_tag_name("img")
        for i in d:

            src = i.get_attribute("src")
            if src.endswith("="):
                print(src)
                urllib.request.urlretrieve(src, "cap.jpg")

                im1 = Image.open('cap.jpg')
                im1.save('cap.png')
                reader = Reader(['en'], gpu=False)

                res = reader.readtext("cap.png", detail=0, paragraph=True)
                print(res)
                add_text = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_txtCaptcha"]')
                for i in res:
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
                        elif j in "-":
                            sub = int(get_num[0]) - int(get_num[1])
                            add_text.send_keys(add)
                            submit = driver.find_element_by_xpath(
                                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
                            print(sub)

    elif lable == "Enter characters as displayed in image":
        print("charaters")
        d = driver.find_elements_by_tag_name("img")
        for i in d:

            src = i.get_attribute("src")
            if src.endswith("="):
                print(src)
                urllib.request.urlretrieve(src, "cap.jpg")

                im1 = Image.open('cap.jpg')
                im1.save('cap.png')
                reader = Reader(['en'], gpu=False)

                res = reader.readtext("cap.png", detail=0, paragraph=True)
                print(res)
                add_text = driver.find_element_by_xpath(
                    '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_txtCaptcha"]')
                for i in res:
                    remve_space = i.replace(" ", "")
                    print(remve_space)
                    add_text.send_keys(remve_space)
                    submit = driver.find_element_by_xpath(
                        '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()

    else:
        print("it is asking for index number")
        driver.close()


def main():
    global lable

    if lable == "Evaluate the Expression":
        print("express here")
        driver.close()
        # continue
        # pass

    elif lable == "Enter characters as displayed in image":
        print("charaters")
    #     image = driver.find_elements_by_xpath(
    #         '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_imgMathCaptcha"]')
    # # print(image)

    #     action_chain = ActionChains(driver)
    #     action_chain.move_to_element(image[0])
    #     screenshot = driver.get_screenshot_as_base64()
    #     im = Image.open(BytesIO(base64.b64decode(screenshot)))
    #     for img in image:
    #         # print("yess : " + str(img))
    #         loc = img.location

    #         siz = img.size

    #     left = loc['x']
    #     top = loc['y']
    #     right = loc['x'] + siz['width']
    #     bottom = loc['y'] + siz['height']
    #     # print(right, bottom)
    #     imgs = im.crop((int(left), int(top), int(right), int(bottom)))
    #     # print(imgs)
    #     imgs.save("click.png")

    #     image = cv2.imread("click.png")
    #     # print(image)
    #     img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #     kernel = np.ones((1, 1), np.uint8)
    #     img = cv2.dilate(img, kernel, iterations=1)
    #     img = cv2.erode(img, kernel, iterations=1)
    #     cv2.imwrite("removed_noise.png", img)

        driver.close()
        # continue
        # pass

    else:
        print("it is asking for index number")
        image = driver.find_elements_by_xpath(
            '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_imgMathCaptcha"]')
    # print(image)

        action_chain = ActionChains(driver)
        action_chain.move_to_element(image[0])
        screenshot = driver.get_screenshot_as_base64()
        im = Image.open(BytesIO(base64.b64decode(screenshot)))
        for img in image:
            # print("yess : " + str(img))
            loc = img.location

            siz = img.size

        left = loc['x']
        top = loc['y']
        right = loc['x'] + siz['width']
        bottom = loc['y'] + siz['height']
        # print(right, bottom)
        imgs = im.crop((int(left), int(top), int(right), int(bottom)))
        # print(imgs)
        imgs.save("click.png"),

        im = Image.open('click.png')
        rgb_img = im.convert('RGB')
        i = rgb_img.save('new_click.jpg', quality=100)

        image = cv2.imread("click.png")
        # print(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        cv2.imwrite("removed_noise.png", img)
        convrt = pytesseract.image_to_string(r'removed_noise.png')
        print(convrt[0])
        print(convrt[1])
        print(convrt[2])
        print(convrt[3])
        print(convrt[4])

        add_text = driver.find_element_by_xpath(
            '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_txtCaptcha"]')

        if "First" in lable:
            first_number = convrt[0]
            add_text.send_keys(first_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        elif "Second" in lable:
            second_number = convrt[1]
            add_text.send_keys(second_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        elif "Third" in lable:
            third_number = convrt[2]
            add_text.send_keys(third_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        elif "Fourth" in lable:
            fourth_number = convrt[3]
            add_text.send_keys(fourth_number)
            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()
        elif "Fifth" in lable:
            fifth_number = convrt[4]
            add_text.send_keys(fifth_number)

            driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_btnSearch"]').click()


def testing():
    filename = "sample.jpg"

    reader = Reader(['en'], gpu=False)

    res = reader.readtext(filename)
    # res = reader.readtext(filename, detail=0, paragraph=True)

    print(res)
    # for text in res:

    #     get_num = re.findall('[0-9]+', str(text))
    #     print(get_num)
    # print(get_num[1])

    # for i in get_num:
    # print(i)

    # display the OCR'd text and associated probability
    # print(text)
    # unpack the bounding box

    # print(res)
    # img = cv2.imread('click.png')
    # img = cv2.resize(img, (620, 480))
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale
    # gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection

    # cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
    #                         cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    # screenCnt = None

    # # loop over our contours
    # for c in cnts:
    #     # approximate the contour
    #     peri = cv2.arcLength(c, True)
    #     approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    #     # if our approximated contour has four points, then
    #     # we can assume that we have found our screen
    #     if len(approx) == 4:
    #         screenCnt = approx
    #         break

    # # Masking the part other than the number plate
    # mask = np.zeros(gray.shape, np.uint8)
    # new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)

    # new_image = cv2.bitwise_and(img, img, mask=mask)

    # # Now crop
    # # (x, y) = np.where(mask == 255)
    # # (topx, topy) = (np.min(x), np.min(y))
    # # (bottomx, bottomy) = (np.max(x), np.max(y))
    # # Cropped = gray[topx:bottomx+1, topy:bottomy+1]

    # # Read the number plate
    # text = pytesseract.image_to_string(new_image, config='--psm 11')
    # print("Detected Number is:", text)

    # cv2.imshow('image', new_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # his = im.histogram()
    # values = {}

    # for i in range(256):
    #     values[i] = his[i]

    # for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
    #     print(j, k)

    # image = cv2.imread("click.png")
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # contrast_img = cv2.addWeighted(
    #     image, 2.5, np.zeros(image.shape, image.dtype), 0, 0)
    # cv2.imshow('Contrast Image', img_gray)
    # cv2.waitKey(0)

    # img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # enhancer = ImageEnhance.Sharpness(image)
    # enhanced_im = enhancer.enhance(10.0)
    # enhanced_im.save("enhanced.png", quality=100)
    # cv2.imwrite("contrast.png", img_gray)

    # convrt = pytesseract.image_to_string(r"getCapchaImage.jpg")
    # print(convrt)


if __name__ == "__main__":
    drivers()
    search_awbno()
    lab()
    solving_captcha()
    # main()
    # testing()

# img_captcha_base64 = driver.execute_async_script("""
#     var ele = arguments[0], callback = arguments[1];
#     ele.addEventListener('load', function fn(){
#       ele.removeEventListener('load', fn, false);
#       var cnv = document.createElement('canvas');
#       cnv.width = this.width; cnv.height = this.height;
#       cnv.getContext('2d').drawImage(this, 0, 0);
#       callback(cnv.toDataURL('image/jpeg').substring(22));
#     }, false);
#     ele.dispatchEvent(new Event('load'));
#     """, image)
# # print(img_captcha_base64)
# with open(r"captcha.jpg", 'wb') as f:
#     f.write(base64.b64decode(img_captcha_base64))

# img_base64 = driver.execute_script("""
# var ele = arguments[0];
# var cnv = document.createElement('canvas');
# cnv.width = 250; cnv.height = 60;
# cnv.getContext('2d').drawImage(ele, 0, 0);
# return cnv.toDataURL('image/jpeg').substring(22);
# """, image)  # "/html/body/form/div[2]/div[3]/span[3]/div[1]/img"))
# with open(r"image.jpg", 'wb') as f:
#     f.write(base64.b64decode(img_base64))
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# import urllib.request

# # options = webdriver.ChromeOptions()
# # # options.add_argument("--headless")
# # # options.headless = True
# # options.add_experimental_option("excludeSwitches", ["enable-logging"])
# # driver = webdriver.Chrome(
# #     options=options, executable_path=r'./chromedriver')


# urllib.request.urlretrieve(
#     "https://www.indiapost.gov.in/_layouts/15/DOP.Portal.UILayer/Captcha.aspx?Ran=hs6dFm8L7y0=", "local-filename.jpg")

# # driver.get(
# #     "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx")

# # # get the image source
# # image = driver.find_elements_by_xpath(
# #     '//*[@id="ctl00_PlaceHolderMain_ucNewLegacyControl_ucCaptcha1_imgMathCaptcha"]')

# # # img = driver.find_element_by_xpath('//img')
# # actionChains = ActionChains(driver)
# # # actionChains.move_to_element(image[0])
# # actionChains.context_click(image[0]).perform()
# # actionChains.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
# # actionChains.send_keys(Keys.ENTER).perform()
