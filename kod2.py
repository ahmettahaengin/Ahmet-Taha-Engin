menu = {
    "pizza" : 75,
    "hamburger" : 65,
    "tavuk" : 55,
    "makarna" : 45
}

print("Mevcut menü: ")
for yemek in menu:
    print(f"{yemek.capitalize()} - {menu[yemek]}")

secim = input("\nFiyatını öğrenmek istediğiniz yemek nedir? ")

if secim in menu:
    print(f"{secim} fiyatı: {menu[secim]} TL")
else:
    print("Bu yemek menüde yok.")

yeni_yemek = input("\nMenüye eklemek istedğiniz yemek: ")
yeni_fiyat = int(input("\nGirdiğiniz yemeğin fiyatı : "))
menu[yeni_yemek] = yeni_fiyat
print(f"\nGüncellenmiş menü")
for yemek in menu:
    print(f"{yemek} - {menu[yemek]} TL")
