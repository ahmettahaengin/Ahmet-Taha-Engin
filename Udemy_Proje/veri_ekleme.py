import sqlite3
'''dersler istinde veri tabanı oluşturuyoruz'''
con = sqlite3.connect("dersler.db")
'''bağlantı nesnesi oluşturuyoruz'''
cursor = con.cursor()
'''tablo oluştur isimli fonksiyon ile ogrenciler isimli bir tablo oluşturuyoruz.'''
ad = input("Ad gir:")
soyad = input("soyad gir:")
numara = int(input("numara gir:"))
notu = int(input("not gir:"))
def tabloolustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, soyad TEXT, numara INT, notu INT)")

'''kayitekle isimli fonksiyonla tablomuza bir adet kayıt ekliyoruz'''
def kayitekle():
    cursor.execute("INSERT INTO ogrenciler VALUES (?,?,?,?)",(ad,soyad,numara,notu))
    con.commit()
    con.close()
'''Oluşturduğumuz fonksiyonları çalıştırarak kayıt ekleme işlemini yapıyoruz.'''
tabloolustur()
kayitekle()