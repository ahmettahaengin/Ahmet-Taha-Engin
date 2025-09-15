from instaUser import username, password
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class Insta:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
        time.sleep(7)  # Wait for the login to complete

    def openFollowers(self):
        # Go to your profile page
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)

        # Find and click the followers link
        followers_link = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "takipçi"))
        )
        followers_link.click()
        time.sleep(5)  # Wait for the followers list to load

        # Find all elements matching the given CSS selector (usernames)
        elements = self.browser.find_elements(By.CSS_SELECTOR,
                                              "[class='_ap3a _aaco _aacw _aacx _aad7 _aade'][dir='auto']")

        # Iterate through the elements and append the text (follower names) to self.followers
        for element in elements[:10]:  # Limit to the first 10 followers for testing
            self.followers.append(element.text)

    def export_followers_to_excel(self):
        df = pd.DataFrame(self.followers, columns=["Follower Name"])
        df.to_excel("Instagram_Followers.xlsx", index=False)
        print("Follower names have been exported to 'Instagram_Followers.xlsx'.")

    def close_browser(self):
        self.browser.quit()

# Usage
instagram = Insta(username, password)
instagram.signIn()
instagram.openFollowers()

# Export the followers to an Excel file
instagram.export_followers_to_excel()

# Close the browser
instagram.close_browser()

# Print the follower names
print(instagram.followers)
