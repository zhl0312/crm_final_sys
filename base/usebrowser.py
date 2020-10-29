
from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.set_headless()
# driver = webdriver.Chrome(chrome_options=opts)


class UseBrowser:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        UseBrowser.driver = self.driver


    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()
