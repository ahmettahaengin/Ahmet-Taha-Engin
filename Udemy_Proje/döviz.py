import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kur.doviz.com/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

isimler = soup.find_all("span",{"class":"name"})
rakamlar = soup.find_all("span",{"class":"value"})
oran = soup.find_all("div",{"class","change-rate status up","change-rate status down"})

for isimler,rakamlar,oran in zip(isimler,rakamlar,oran):
    print("-->",isimler.text)
    print("-->",rakamlar.text)
    print("-->",oran.text.lstrip())

df = pd.DataFrame({"İsimler":isimler})
df = pd.DataFrame({"Rakamlar":rakamlar})
df = pd.DataFrame({"Oran":oran})

df.to_csv("İsimler.csv","Rakamlar.csv","Oran.csv")