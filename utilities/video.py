from selenium import webdriver

driver = None

def play(video_url):
    global driver
    url = video_url
    driver = webdriver.Edge()
    driver.get(url)

def quit():
    global driver
    if driver is not None:
        driver.quit()
