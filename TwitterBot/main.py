import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class RonaldoSubsTwitterBot:
    def __init__(self):
        self.chromeoptions = webdriver.ChromeOptions()
        self.chromeoptions.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.chromeoptions)
        self.ronaldosubs=""
        self.beastsubs = ""

    def get_subs_Ronaldo(self):
        self.driver.get("https://www.youtube.com/@cristiano")

        time.sleep(3)
        subcount=self.driver.find_element(By.XPATH,value='//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
        self.ronaldosubs=subcount.text

    def get_subs_Beast(self):
        self.driver.get("https://www.youtube.com/@MrBeast")

        time.sleep(3)
        subcountbeast=self.driver.find_element(By.XPATH,value='//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
        self.beastsubs=subcountbeast.text

    def tweet_it_out(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(35)
        sendmessage = self.driver.find_element(By.XPATH,"*//*[@contenteditable='true']")
        sendmessage.send_keys(f"MrBeast has {self.beastsubs}.\nCristiano Ronaldo has now reached {self.ronaldosubs}.\nSiuuuuuuuu!")

        time.sleep(5)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()


bot = RonaldoSubsTwitterBot()
bot.get_subs_Ronaldo()
bot.get_subs_Beast()
bot.tweet_it_out()
