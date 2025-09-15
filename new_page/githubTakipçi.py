from githubUserInfo import username, password
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()

    def getFollowers(self):
        self.browser.get("https://github.com/I-aTe?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")  # Düzeltme: find_elements

        for item in items:
            follower_name = item.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text  # Düzeltme: Doğru CSS seçici
            self.followers.append(follower_name)


github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)
