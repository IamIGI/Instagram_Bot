from InstagramFollowBot import InstagramBot

CHROME_DRIVER_PATH = "G:\Learning Python\Projects\Day52-repeat\chromedriver.exe"
INSTAGRAM_EMAIL = "testemail1998123@gmail.com"
INSTAGRAM_PASSWORD = "PythonBotProjects123xD"
INSTAGRAM_LOGIN_WEBSITE = "https://www.instagram.com/"
TARGET_ACCOUNT = "python.hub"

Bot = InstagramBot(PATH=CHROME_DRIVER_PATH)

Bot.login(INSTAGRAM_LOGIN=INSTAGRAM_EMAIL, INSTAGRAM_PASSWORD=INSTAGRAM_PASSWORD)
Bot.find_followers(TARGET_ACCOUNT=TARGET_ACCOUNT)
Bot.follow()
