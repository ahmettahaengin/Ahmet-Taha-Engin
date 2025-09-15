import pandas as pd

# TXT dosyasının yolu
txt_dosya = "veriler.txt"
excel_dosya = "veriler.xlsx"
# TXT dosyasını oku (örneğin tab ile ayrılmışsa delimiter="\t")
df = pd.read_csv(txt_dosya, delimiter="\t")

# Excel olarak kaydet
df.to_excel(excel_dosya, index=False)

print("Dönüştürme tamamlandı:", excel_dosya)
