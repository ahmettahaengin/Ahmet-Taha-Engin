import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://google.com/")

    print(driver.title)

    text_box = driver.find_element(by=By.NAME, value="q")
    text_box.send_keys("Google")
    text_box.send_keys(Keys.ENTER)

    time.sleep(10)  # Test için bekleme süresini kısalttım
    driver.quit()
