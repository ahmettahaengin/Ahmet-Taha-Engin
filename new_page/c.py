import re
import pandas as pd

# Dosya yolu
dosya = "veriler.txt"
excel_dosya = "whatsapp_mesajlar.xlsx"

# Sonuçları saklayacağımız liste
veriler = []

# Dosyayı satır satır oku
with open(dosya, "r", encoding="utf-8") as f:
    for satir in f:
        # Mesaj formatı: "tarih - kişi: mesaj"
        eslesme = re.match(r"(\d{1,2}\.\d{1,2}\.\d{4} \d{1,2}:\d{2}) - (.*?): (.*)", satir)
        if eslesme:
            tarih = eslesme.group(1)
            kisi = eslesme.group(2)
            mesaj = eslesme.group(3)

            # İstemediğimiz satırları filtrele
            if not any(x in mesaj for x in ["IMG-", "Bu mesaj silindi", "dosya ekli", "grubunu oluşturdu", "ekledi"]):
                veriler.append([tarih, kisi, mesaj])

# DataFrame oluştur
df = pd.DataFrame(veriler, columns=["Tarih", "Kişi", "Mesaj"])

# Excel olarak kaydet
df.to_excel(excel_dosya, index=False)

print("İşlem tamamlandı:", excel_dosya)
