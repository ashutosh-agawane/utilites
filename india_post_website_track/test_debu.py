# # from selenium import webdriver
# # from Screenshot import Screenshot_Clipping

# # # browser exposes an executable file
# # # Through Selenium test we will invoke the executable file which will then

# # # invoke actual browser
# # ob = Screenshot_Clipping.Screenshot()
# # options = webdriver.ChromeOptions()

# # # options.headless = True
# # options.add_experimental_option("excludeSwitches", ["enable-logging"])
# # driver = webdriver.Chrome(
# #     options=options, executable_path=r'./chromedriver')
# # # to maximize the browser window

# # driver.maximize_window()
# # # get method to launch the URL
# # driver.get(
# #     "https://www.indiapost.gov.in/_layouts/15/DOP.Portal.Tracking/TrackConsignment.aspx")
# # # to refresh the browser
# # loading_page = driver.page_source

# # img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
# # print(img_url)
# # # def S(X): return driver.execute_script(
# # #     'return document.body.parentNode.scroll'+X)


# # # driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
# # # driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
# # # driver.refresh()
# # # # to get the screenshot of complete page
# # # driver.save_screenshot("screenshot_tutorialspoint.png")
# # # to close the browser
# # driver.close()
# # import pdfkit
# from pyhtml2pdf import converter
# import os
# path = os.path.abspath('index.html')
# converter.convert(f'file:///{path}', 'sample.pdf')

# # pdfkit.from_string()
# # import csv

# # import pandas as pd

# # df = pd.read_csv("Transaction-Details (1).csv", skiprows=9, names=["SNo.", "Terminal ID", "Merchant Name", "Location", "Customer ID/Card PAN", "Vehicle No.", "Txn ID",
# #                                                                    "Txn Date", "Txn Type", "Txn Mode", "Txn Mode Value", "Product", "Currency", "RSP", "Quantity", "Amount", "Balance", "Entitled CashBack", "Odometer", "Status"])
# # print(df["Txn Date"].str.ma)
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
import json
import os
import codecs
import pdfkit
options = Options()
# appState = {
#     "recentDestinations": [
#         {
#             "id": "Save as PDF",
#             "origin": "local"
#         }
#     ],
#     "selectedDestinationId": "Save as PDF",
#     "version": 2
# }

# profile = {
#     'printing.print_preview_sticky_settings.appState': json.dumps(appState)}
# profile = {'printing.print_preview_sticky_settings.appState':json.dumps(appState),'savefile.default_directory':downloadPath}
# options.add_experimental_option('prefs', profile)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--kiosk-printing')
CHROMEDRIVER_PATH = './chromedriver'

driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)
driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/index.htm")
path = r"E:\python\data\india_post_website_track"
n = os.path.join(path, "Page.html")
f = codecs.open(n, "w", "utf−8")
# obtain page source
h = driver.page_source
# write page source content to file
f.write(h)
p = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=p)
pdfkit.from_file('Page.html', 'out.pdf', configuration=config)
# close browser
driver.quit()
