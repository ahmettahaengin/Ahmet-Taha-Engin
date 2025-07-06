# Menü tanımlama
menu = {
    "pizza": 75,
    "hamburger": 55,
    "tavuk": 60,
    "makarna": 45
}

# 1. Menüdeki yemekleri yazdır
print("Mevcut Menü:")
for yemek in menu:
    print(f"{yemek.capitalize()} - {menu[yemek]} TL")

# 2. Kullanıcıdan yemek ismi al, fiyatını göster
secim = input("\nFiyatını öğrenmek istediğiniz yemek nedir? ").lower()
if secim in menu:
    print(f"{secim.capitalize()} fiyatı: {menu[secim]} TL")
else:
    print("Bu yemek menüde yok.")

# 3. Menüye yeni yemek ekle
yeni_yemek = input("\nMenüye eklemek istediğiniz yeni yemek: ").lower()
yeni_fiyat = int(input("Yeni yemeğin fiyatı (sadece sayı): "))
menu[yeni_yemek] = yeni_fiyat
print(f"\nGüncellenmiş Menü:")
for yemek in menu:
    print(f"{yemek.capitalize()} - {menu[yemek]} TL")
