from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class InstaFollower:
    def __init__(self, ser):
        self.driver = webdriver.Chrome(service=ser)

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(1)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[4]/div/div/button[1]').click()
        sleep(2)
        email_field = self.driver.find_element(By.XPATH,
                                                  '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.XPATH,
                                                  '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()

    def find_followers(self, target):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{target}/")
        sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        sleep(4)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        print(follow_buttons)
        for button in follow_buttons:
            button.click()
            sleep(1)
        