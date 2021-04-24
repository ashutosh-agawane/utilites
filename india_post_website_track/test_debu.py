from selenium import webdriver
from Screenshot import Screenshot_Clipping

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then

# invoke actual browser
ob = Screenshot_Clipping.Screenshot()
options = webdriver.ChromeOptions()

# options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r'./chromedriver')
# to maximize the browser window

driver.maximize_window()
# get method to launch the URL
driver.get(
    "https://www.indiapost.gov.in/_layouts/15/DOP.Portal.Tracking/TrackConsignment.aspx")
# to refresh the browser
loading_page = driver.page_source

img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
# def S(X): return driver.execute_script(
#     'return document.body.parentNode.scroll'+X)


# driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
# driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
# driver.refresh()
# # to get the screenshot of complete page
# driver.save_screenshot("screenshot_tutorialspoint.png")
# to close the browser
driver.close()
