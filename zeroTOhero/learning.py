import random

from fontTools.ttLib import tagToIdentifier

low = int(input("Aralığın taban sayısını gir: "))
high = int(input("Aralığın tavan sayısını gir: "))

tahmin_sayısı = int(input("Tahmin sayısını gir : "))

yapılan_tahmin = 0

sayı = random.randint(low, high)

while True:

    denenen_sayı = int(input("Bir sayı tahmin et: "))

    yapılan_tahmin += 1
    print(f"Yaptığın tahmin sayısı : {yapılan_tahmin}")
    if yapılan_tahmin == tahmin_sayısı:
        print("Tahimn hakkın bitti tekrar dene.")
        break


    if denenen_sayı < sayı:
        print("Daha büyük bir sayı dene.")

    elif denenen_sayı > sayı:
        print("Daha küçük bir sayı dene.")

    if denenen_sayı == 0:
        break

    elif denenen_sayı == sayı:
        print(f"Doğru tahmin ettin sayı : {sayı}")
        break
        