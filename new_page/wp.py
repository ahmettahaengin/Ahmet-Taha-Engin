import pyautogui
import time

count = int(input("Sayı : "))

message = input("Mesaj : ")

time.sleep(5)

while(count>0):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")
    count -= 1
print("Sonlandı")