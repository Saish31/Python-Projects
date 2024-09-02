import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class RonaldoSubsTwitterBot:
    def __init__(self):
        self.chromeoptions = webdriver.ChromeOptions()
        self.chromeoptions.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chromeoptions)
        self.tweet=""

    def get_subs(self):
        self.driver.get("https://www.youtube.com/@cristiano")

        time.sleep(3)
        subcount=self.driver.find_element(By.XPATH,value='//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
        self.tweet=subcount.text

    def tweet_it_out(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(35)
        sendmessage = self.driver.find_element(By.XPATH,"*//*[@contenteditable='true']")
        sendmessage.send_keys(f"Cristiano Ronaldo has now reached {self.tweet} on Youtube.\nSiuuuuuuuu!")

        time.sleep(5)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()


bot = RonaldoSubsTwitterBot()
bot.get_subs()
bot.tweet_it_out()
