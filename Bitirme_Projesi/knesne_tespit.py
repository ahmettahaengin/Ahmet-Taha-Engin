import serial
import cv2
import numpy as np
import time

ser = serial.Serial("COM9", 9600, timeout=1)
x = cv2.VideoCapture(0)

sayac = 0

while(x.isOpened()):

    sayac = sayac + 1
    ret, frame = x.read()
    # kırmızı renk tespiti
    xGri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    xRed = frame[:,:,0]
    kirmizirenk = cv2.subtract(xRed,xGri)
    z,xIkili= cv2.threshold(kirmizirenk,75,255,cv2.THRESH_BINARY)
    kernel = np.ones((2,2), np.uint8)
    xIkili = cv2.erode(xIkili, kernel, iterations=10)

    (toplamBlob, etiket_id, degerler, centroid) = cv2.connectedComponentsWithStats(xIkili, 4, cv2.CV_32S)
    print("sayac: "+str(sayac)+ " "+str(toplamBlob))

    if(toplamBlob>1):
        komut = "ON"
        ser.write(komut.encode("utf-8"))
        time.sleep(1)
        print("Burda kırmızı nesne var.")

    else:
        komut = "OFF"
        ser.write(komut.encode("utf-8"))
    cv2.imshow("frame",frame)
    cv2.imshow("Ikili",xIkili)
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
ser.close()
x.release()
cv2.destroyAllWindows()