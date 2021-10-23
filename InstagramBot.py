from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self,USERNAME, PASSWORD):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(USERNAME)
        self.driver.find_element_by_name("password").send_keys(PASSWORD)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(4)
        # self.driver.find_element_by_css_selector(".mt3GC .HoLwm").click()

    def find_followers(self, TARGET_ACCOUNT):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        self.driver.find_element_by_partial_link_text("obserwujących").click()
        time.sleep(2.0)
        
        #Followers Pop-up
        for i in range(4):
            #Find the first anchor that in the popup
            #This need to be renewed each time as the list scrolls.
            self.find_element('/html/body/div[6]/div/div/div[2]//a').send_keys(Keys.END)
            # "//a" - find another anchor tag below  given XPATH
            time.sleep(2)


    def find_element(self, xpath):
        while True:
            try:
                element = self.driver.find_element_by_xpath(xpath)
                return element
            except common.exceptions.ElementNotInteractableException:
                print("ElementNotInteractableException")
            except common.exceptions.NoSuchElementException:
                print("NoSuchElementException")
            finally:
                time.sleep(1)

    def follow(self):
        self.Follower_list = self.driver.find_elements_by_css_selector(".wo9IH .uu6c_ .Pkbci button")
        print(len(self.Follower_list))
        for element in self.Follower_list:
            # element.click()
            try:
                element.click()
            except common.exceptions.ElementClickInterceptedException:
                print("ElementClickInterceptedException")
                pass



