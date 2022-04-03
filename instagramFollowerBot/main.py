from selenium.webdriver.chrome.service import Service
from InstaFollower import InstaFollower

CHROME_WEBDRIVER_PATH = "The Path to your chrome webdriver"
SIMILAR_ACCOUNT = "Enter the account you want to follow all followers from"
EMAIL = "Insta Email"
PASSWORD = "Insta Password"

ser = Service(CHROME_WEBDRIVER_PATH)

bot = InstaFollower(ser)

bot.login(EMAIL, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
