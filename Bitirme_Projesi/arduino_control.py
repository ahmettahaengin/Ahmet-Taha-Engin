import serial
import time
import struct

# Seri portu tanımla
ser = serial.Serial('COM9', 9600,timeout=1) # Seri portun açılması için kısa bir süre bekle

def send_command(command, speed):
    ser.write(command.encode())
    ser.write(struct.pack('f', speed))

def calculate_speed_from_y_coordinate(y):
    # Örnek bir hesaplama: Hızın y koordinatı ile nasıl hesaplanacağını belirleyin
    speed = 1000 - (3*y)  # Bu sadece örnek bir hesaplama, y'ye bağlı olarak hız değişir
    return speed

try:
    with open('detected_points_y.txt', 'r') as file:
        for line in file:
            y = float(line.strip())  # Her satırda sadece y ekseni değeri var
            speed = calculate_speed_from_y_coordinate(y)
            send_command('1', speed)
            print(f"Y Koordinatı: {y}, Hesaplanan Hız: {speed}")
            time.sleep(5)  # Komutlar arasında bekleme süresi

except KeyboardInterrupt:
    print("Kullanıcı tarafından durduruldu.")
finally:
    ser.close()
    print("Seri port kapatıldı.")
