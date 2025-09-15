vize1 = input("Vize: ")
final = input("Final: ")

sonuc = int(vize1)*(4/10) + int(final)*(6/10)

if(sonuc >=90):
    print("Harf Notu: AA")
elif(sonuc>=85):
    print("Harf Notu: BA")
elif(sonuc>=80):
    print("Harf Notu: BB")
elif(sonuc>=75):
    print("Harf Notu: CB")
elif(sonuc>=70):
    print("Harf Notu: CC")
elif(sonuc>=65):
    print("Harf Notu: DC")
elif(sonuc>=60):
    print("Harf Notu: DD")
elif(sonuc>=55):
    print("Harf Notu: FF")
print("Ortalama")
print(sonuc)