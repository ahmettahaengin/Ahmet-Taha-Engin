import requests
from bs4 import BeautifulSoup

r = "https://borsa.doviz.com/"

response = requests.get(r)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


value = soup.find_all("tr",{"role":"row"})

for value in value:
    print("------",value.text)