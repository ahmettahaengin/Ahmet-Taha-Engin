import time
import serial
ser = serial.Serial("COM9", 9600, timeout=1)

# Dosyayı açın
with open("detected_points.txt", "r") as dosya:
    # Her satırı okuyun
    for satir in dosya:
        # Satırı ikiye ayırın
        x, y = satir.split(",")

        # Koordinatları robota gönderin
        ser.write(f"x:{x},y:{y}".encode('utf-8'))
        time.sleep(1)

# Bağlantıyı kapatın
ser.close()