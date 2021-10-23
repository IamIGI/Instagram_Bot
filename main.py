from InstagramBot import InstagramBot

CHROME_DRIVER_PATH = ""                                              #path to chromedriver.exe
INSTAGRAM_EMAIL = ""                                                 #Instagram Email
INSTAGRAM_PASSWORD = ""                                              #Instagram Password
INSTAGRAM_LOGIN_WEBSITE = "https://www.instagram.com/"
TARGET_ACCOUNT = "python.hub"                                        #target_account

InstFollower = InstagramBot(path=CHROME_DRIVER_PATH)

InstFollower.login(USERNAME=INSTAGRAM_EMAIL, PASSWORD=INSTAGRAM_PASSWORD)
InstFollower.find_followers(TARGET_ACCOUNT=TARGET_ACCOUNT)
InstFollower.follow()
