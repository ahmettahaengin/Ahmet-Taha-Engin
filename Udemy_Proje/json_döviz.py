import requests
import sys

url = " sadgsadg "

birinci_döviz = input("Birinci Döviz :")
ikinci_döviz = input("İkinci Döviz :")
miktar = float(input("Miktar :"))

response = requests.get(url + birinci_döviz)

json_verisi = response.json()

try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)
except KeyError:
    sys.stderr.wrtie("Lütfen para birimlerini doğru girin.")
    sys.stderr.flush()