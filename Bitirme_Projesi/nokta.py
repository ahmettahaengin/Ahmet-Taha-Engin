import cv2

# Görüntüyü yükle
image_path = "bdot_1.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Siyah renk aralığını belirle (0, 0, 0) - (0, 0, 0)
lower_black = (0, 0, 0)
upper_black = (0, 0, 0)

# Görüntüyü siyah renk aralığına göre maskele
mask = cv2.inRange(image, lower_black, upper_black)

# Siyah noktaları tespit et
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1:  # Minimum alanı belirle
        x, y, w, h = cv2.boundingRect(contour)
        detected_point = (int(x + w / 2), int(y + h / 2))
        print("Detected Black Point Coordinates:", detected_point)
        cv2.circle(image, detected_point, 5, (0, 255, 0), -1)  # Tespit edilen noktayı çiz

# Tespit edilen noktayı göster
cv2.imshow('Detected Points', image)
cv2.waitKey()
cv2.destroyAllWindows()

# Koordinatları tutmak için bir liste oluştur
detected_points = []

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1:  # Minimum alanı belirle
        x, y, w, h = cv2.boundingRect(contour)
        detected_point = (int(x + w / 2), int(y + h / 2))
        detected_points.append(detected_point[1])  # Sadece y ekseni koordinatını al

# Y ekseni koordinatlarını dosyaya yaz
output_file = "detected_points_y.txt"
with open(output_file, 'w') as file:
    for y in detected_points:
        file.write(f"{y}\n")

print(f"Detected points are written to {output_file}")
