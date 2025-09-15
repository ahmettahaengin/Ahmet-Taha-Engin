import cv2
import serial
import time

# Seri bağlantı oluştur
ser = serial.Serial('COM9', 9600,timeout=1)  # Arduino'nun bağlı olduğu COM portunu ve baud hızını belirtin

# Görüntüyü yükle
image_path = "siyahnokta2.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Siyah renk aralığını belirle (0, 0, 0) - (0, 0, 0)
lower_black = (0, 0, 0)
upper_black = (0, 0, 0)

# Görüntüyü siyah renk aralığına göre maskele
mask = cv2.inRange(image, lower_black, upper_black)

# Siyah noktaları tespit et
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Koordinatları tutmak için bir liste oluştur
detected_points = []

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1:  # Minimum alanı belirle
        x, y, w, h = cv2.boundingRect(contour)
        detected_point = (int(x + w / 2), int(y + h / 2))
        detected_points.append(detected_point)

# Koordinatları Arduino'ya gönder
for point in detected_points:
    # Koordinatları seri iletişim protokolüne uygun bir şekilde kodla
    point_str = f"{point[0]},{point[1]}\n"  # Örneğin, 100,200\n gibi

    # Koordinatları Arduino'ya gönder
    ser.write(point_str.encode())

    # Arduino'nun cevabını beklemek için kısa bir süre bekle (opsiyonel)
    time.sleep(0.1)
print(detected_points)
# Seri bağlantıyı kapat
ser.close()