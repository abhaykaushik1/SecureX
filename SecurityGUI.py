from tkinter import *
from PIL import Image, ImageTk
import face_recognition


def display():
    window = Tk()
    window.geometry("400x400")
    window.title("byteMe app")
    window.configure(bg="black")

    im = Image.open('locked.png')
    ph = ImageTk.PhotoImage(im)
    button = Button(window, image=ph, bg="black", command=command).place(x=75,
                                                                         y=75)
    message = Message(window, text="PRESS TO UNLOCK", bg="black", fg="white",
                      width=250, aspect=100).place(x=150, y=50)
    window.mainloop()


def command():
    face_recognition.run_face_recognition()
