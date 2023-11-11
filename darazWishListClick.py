import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import getpass


class darazWishListClick:
    def __init__(self):
        chrome_options = Options()
        try:
            chrome_options.add_argument(
                "--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(
                    getpass.getuser()
                )
            )
            chrome_options.add_argument("--profile-directory=Profile 1")
            self.driver = webdriver.Chrome(options=chrome_options)
        except:
            self.driver = webdriver.Chrome()

    def loin(self):
        btniID = ".mod-third-party-login-google"
        googleLogBtn = self.driver.find_element(By.CSS_SELECTOR, value=btniID)
        googleLogBtn.click()

    def openNewLink(self, link):
        self.driver.get(link)

    def clickWishListBtn(self):
        if not os.path.exists("settings.txt"):
            open("settings.txt", "w").close()
        file = open("settings.txt", "r")
        btniID = file.read()
        try:
            wish_list = self.driver.find_element(value=btniID)
            wish_list.click()
        except:
            pass
