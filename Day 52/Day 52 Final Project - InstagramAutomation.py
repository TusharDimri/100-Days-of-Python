import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

USERNAME="just_for_testing2000"
PASSWORD="Tushar$7983"
TARGET_ACCOUNT='mutantmmacademydehradun/'


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = 'https://www.instagram.com/'
        self.people = []

    def follow(self):
        for person in self.people:
            try:
                person.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                # cancel = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancel')]")
                # cancel.click()
                # time.sleep(3)
                continue
                

    def find_followers(self):
        time.sleep(3)
        url =""
        url = self.url + TARGET_ACCOUNT + 'followers'
        self.driver.get(url)
        time.sleep(5.0)
        popup = self.driver.find_element(By.CLASS_NAME, value='_aano')
        for i in range(2):
            self.people += self.driver.find_elements(By.CLASS_NAME, value='_ap30')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)
            
            
    def login(self):
        self.driver.get(self.url)
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        confirm = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        confirm.click()
        self.find_followers()


bot = InstaFollower()
bot.login()
bot.follow()