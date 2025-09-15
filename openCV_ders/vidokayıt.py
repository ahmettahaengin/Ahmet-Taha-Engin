# Kütüphaneyi import ediyoruz
import cv2

# Cihazın kendi kamerasına erişme
kamera = cv2.VideoCapture(0)  # kamera = cv2.VideoCapture('dosya_adi')

# Video için format belirleme
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' formatını kullanabilirsiniz, ayrıca 'XVID' de kullanılabilir

# Video kaydetme
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# Kameranın açık olup olmadığını kontrol etme
while(kamera.isOpened()):
    ret, cerceve = kamera.read()
    if ret == True:
        # Videonun yükseklik ve genişlik değerlerini döndürür
        print(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Görüntüyü griye çevirme
        gri = cv2.cvtColor(cerceve, cv2.COLOR_BGR2GRAY)

        # Videoyu kaydetmek için
        out.write(cerceve)

        # Videoyu açmak için
        cv2.imshow('Video Basligi', gri)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

kamera.release()
out.release()
cv2.destroyAllWindows()
