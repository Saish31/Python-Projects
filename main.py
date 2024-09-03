import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT=input("Which page do you want to follow? ")
USERNAME=os.environ["INSTA_USERNAME"]
PASSWORD=os.environ["PASSWORD"]


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        login=self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]')
        login.click()
        time.sleep(3)

        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_account(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}/")

    def follow(self):
        time.sleep(3)
        follow_button=self.driver.find_element(By.XPATH,"//*[text()='Follow']")
        follow_button.click()


bot = InstaFollower()
bot.login()
bot.find_account()
bot.follow()
