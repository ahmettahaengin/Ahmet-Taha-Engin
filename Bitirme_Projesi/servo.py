import serial
import time

# Seri bağlantıyı oluştur
ser = serial.Serial("COM9", 9600, timeout=1)  # Arduino'nun bağlı olduğu COM portunu ve baud hızını belirtin

def send_angle(angle):
    if 0 <= angle <= 360:
        # Açıyı seri port üzerinden gönder
        angle_str = f"{angle}\n"
        ser.write(angle_str.encode())
        print(f"Gönderilen açı: {angle}")

        # Arduino'nun cevabını beklemek için kısa bir süre bekle (opsiyonel)
        time.sleep(0.1)
    else:
        print("Geçersiz açı değeri. 0-360 arasında bir değer girin.")

try:
    while True:
        # Kullanıcıdan açı değeri al
        angle_input = input("Açı değeri girin (0-360) veya çıkmak için 'q' tuşuna basın: ")
        if angle_input.lower() == 'q':
            print("Program sonlandırılıyor...")
            break
        try:
            angle = int(angle_input)
            send_angle(angle)
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
except KeyboardInterrupt:
    print("Program sonlandırıldı.")
finally:
    # Seri bağlantıyı kapat
    ser.close()
