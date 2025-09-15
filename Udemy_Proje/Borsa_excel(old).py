import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://uzmanpara.milliyet.com.tr/canli-borsa/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

isim = soup.find_all("b")

liste_isim = []
liste_fiyat = []
liste_yüzde = []
liste_zaman = []

for isim in isim:
	liste_isim.append(isim.text)

for i in range(len(liste_isim)):
	veri = soup.find("td", {"id": f"h_td_fiyat_id_{liste_isim[i]}"})
	if veri:
		liste_fiyat.append(veri.text.strip())
	else:
		liste_fiyat.append("Veri Bulunamadı")
#print(liste_fiyat)

for j in range(len(liste_isim)):
	yüzde = soup.find("td", {"id": f"h_td_yuzde_id_{liste_isim[j]}"})
	if yüzde:
		liste_yüzde.append(yüzde.text.strip())
	else:
		liste_yüzde.append("Veri Bulunamadı")

for k in range(len(liste_isim)):
	zaman = soup.find("td", {"id": f"h_td_zaman_id_{liste_isim[k]}"})
	if zaman:
		liste_zaman.append(zaman.text.strip())
	else:
		liste_zaman.append("Veri Bulunamadı")

liste_borsa = zip(liste_isim,liste_fiyat,liste_yüzde,liste_zaman)

data = []

for liste_borsa in liste_borsa:
	data.append(liste_borsa)
	print(liste_borsa)


df = pd.DataFrame({"BorsaData":data})

df.to_csv("BorsaData.csv")
