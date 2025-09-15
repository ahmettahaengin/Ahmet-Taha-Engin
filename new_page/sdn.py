# import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.chrome.options import Options
import pandas as pd
"""
# Tarayıcı seçeneklerini oluştur
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless modu etkinleştirir

# Tarayıcıyı başlat
driver = webdriver.Chrome(options=chrome_options)
"""
driver = webdriver.Chrome()

haberler = []

i = 1
while i < 3:

    # Web sitesini aç
    driver.get(f"https://shiftdelete.net/haberler/page/{i}")

    section = driver.find_element(By.XPATH, "//*[@id='wrapper']")
    # Tüm <h4> etiketlerini bul
    links = section.find_elements(By.TAG_NAME, "h4")

    # Her <h4> etiketinin metnini yazdır
    for link in links:
        text = link.text
        if text:  # Metin boş değilse yazdır
            haberler.append(text)
    i += 1

for index, haber in enumerate(haberler, start=1):
    print(f"{index}. {haber}")

haberler_data = {"No": list(range(1, len(haberler) + 1)), "Haber Başlığı": haberler}
df = pd.DataFrame(haberler_data)

# Excel dosyasına yaz
df.to_excel("haberler.xlsx", index=False)

print("Excel dosyası başarıyla oluşturuldu: haberler.xlsx")
