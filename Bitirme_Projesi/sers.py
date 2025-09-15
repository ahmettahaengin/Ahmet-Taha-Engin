import tkinter.ttk
import cv2
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("900x900")
window.title("ders")

canvas_top = tkinter.Canvas(window, background="red", height=500, width=800)

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

label_camera = tkinter.Label(canvas_top)
label_camera.place(relx=1,rely=0,anchor="ne")

def show_frame():
    _, frame = cap.read()

    frame = cv2.resize(frame,(300,300), cv2.INTER_LINEAR)
    cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(img)
    print("CAMERA")
    label_camera.imgtk = imgtk
    label_camera.configure(image=imgtk)

    label_camera.after(10,show_frame)

show_frame()


canvas_top.pack(side="top")

canvas_bot = tkinter.Canvas(window,
                            background="black",
                            )

button = tkinter.Button(canvas_bot,
                        text="TIKLA",
                        font=("Arial", 24, "bold"),
                        command=lambda: servo_degeri.set(90))
button.place(relx=0, rely=1, anchor="sw", width=300, height=150, x=10, y=-20)

servo_degeri = tkinter.IntVar()
scale = tkinter.ttk.Scale(canvas_bot,
                          length=200,
                          from_=0,
                          to=180,
                          command=lambda gdgd: print(servo_degeri.get()),
                          variable=servo_degeri)
scale.place(relx=1, rely=0, anchor="ne")

canvas_bot.pack(fill="x", side="bottom")

window.mainloop()
