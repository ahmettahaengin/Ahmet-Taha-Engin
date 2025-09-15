import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"lxml")
	#veriler = soup.find_all("td",class_="center")
	isim = soup.find_all("b")
	liste_isim = []
	liste_fiyat = []
	liste_yüzde = [] 
	liste_zaman = []
	data = []
	for isim in isim:
		liste_isim.append(isim.text)
	for i in range(len(liste_isim)):
		price = soup.find("td", {"id": f"h_td_fiyat_id_{liste_isim[i]}"})
		if price:
			liste_fiyat.append(price.text.strip())
		else:
			liste_fiyat.append("Veri Bulunamadı")

	for j in range(len(liste_isim)):
		yüzde = soup.find("td", {"id": f"h_td_yuzde_id_{liste_isim[j]}"})
		if yüzde:
			liste_yüzde.append(yüzde.text.strip())
		else:
			liste_yüzde.append("Veri Bulunamadı")

	for k in range(len(liste_isim)):
		zaman = soup.find("td",{"id": f"h_td_zaman_id_{liste_isim[k]}"})
		if zaman:
			liste_zaman.append(zaman.text.strip())
		else:
			liste_zaman.append("Veri Bulunamadı")

	for j in range(len(liste_fiyat)):
		item = {}
		item["İsim"] = liste_isim[j]
		item["Fiyat"] = liste_fiyat[j]
		item["Yüzde"] = liste_yüzde[j]
		item["Zaman"] = liste_zaman[j]
		data.append(item)
	return data

def export_data(data):
	df = pd.DataFrame(data)
	df.to_csv("Borsa_Data.csv")
	df.to_excel("Borsa_Data.xlsx")

if __name__ == "__main__":
	data =get_data("https://uzmanpara.milliyet.com.tr/canli-borsa/")
	export_data(data)
	print("Done")