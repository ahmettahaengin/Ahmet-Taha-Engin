from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = r"C:\Users\engin\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()