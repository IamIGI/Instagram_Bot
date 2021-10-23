from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, PATH):
        """ Need path to chromedriver """
        self.driver = webdriver.Chrome(executable_path=PATH)

    def login(self, INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD):
        """ Login to instagram account"""
        #Instagram site
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        #Input login and password to input tabs
        self.driver.find_element_by_name("username").send_keys(INSTAGRAM_LOGIN)
        self.driver.find_element_by_name("password").send_keys(INSTAGRAM_PASSWORD)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(4.5)

        #Turn off notifications
        self.driver.find_element_by_css_selector(".mt3GC .HoLwm").click()

    def find_followers(self, TARGET_ACCOUNT):
        #Open followers pop-up window
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        self.driver.find_element_by_partial_link_text("obserwujących").click()
        time.sleep(2.0)
        
        #Pop_Up window
        for i in range(4):
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]//a').send_keys(Keys.END)
            time.sleep(1.0)

    def follow(self):
        #Get follower list
        self.Follower_list = self.driver.find_elements_by_css_selector(".wo9IH .uu6c_ .Pkbci button")
        print(len(self.Follower_list))
        #AutofollowerBot
        for account in self.Follower_list:
            try:
                account.click()
            except common.exceptions.ElementClickInterceptedException:
                print("ElementClickInterceptedException")
                pass


