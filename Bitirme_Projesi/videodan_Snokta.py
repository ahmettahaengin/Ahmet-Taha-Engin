import cv2
import serial
import time
import os

# Set up the camera
camera = cv2.VideoCapture(0)

# Set up the serial connection
ser = serial.Serial('COM13', 9600, timeout=1)

while True:
    # Capture an image from the camera
    ret, image = camera.read()
    if not ret:
        break

    # Save the image to a file
    timestamp = int(time.time())
    filename = f"image_{timestamp}.png"
    cv2.imwrite(filename, image)

    # Convert the image to grayscale and apply thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a list to store the detected points
    detected_points = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1:  # Set a minimum area threshold
            x, y, w, h = cv2.boundingRect(contour)
            detected_point = (int(x + w / 2), int(y + h / 2))
            detected_points.append(detected_point)

    # Send the detected points to Arduino
    for point in detected_points:
        point_str = f"{point[0]},{point[1]}\n"  # Format the point as a string
        ser.write(point_str.encode())  # Send the point to Arduino
        time.sleep(0.1)  # Optional: wait for a short period

    print(detected_points)  # Print the detected points

    # Close the serial connection
    ser.close()

    # Release the camera resource
    camera.release()
    cv2.destroyAllWindows()
    break