from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from src.views.styles import *
from src.views.functions import *

def resize_image(event):
    width, height = event.width, event.height
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(image_item, image=resized_photo)
    canvas.image = resized_photo
    canvas.configure(width=width, height=height)

def createWindow():
    global image, canvas, image_item

    window = Tk()
    window.title("myPDF.mp3")
    window.minsize(800, 600)
    window.maxsize(800, 600)

    canvas = Canvas(window, width=800, height=600)
    canvas.pack()

    image = Image.open("./windows/src/images/background.jpeg")
    image = image.resize((800, 600), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_item = canvas.create_image(0, 0, anchor='nw', image=photo)

    text = Label(canvas, text="transforme seu tempo em um áudio!".upper(), fg="white")
    txt_dir = Label(canvas, text="Salvar em:", fg="white")
    txt_finish = Label(canvas, text="Finalizado!".upper(), fg="white")
    
    button1 = Button(canvas, text="selecionar arquivo PDF", command=intoFile)
    diretory = Button(canvas, text="Diretório", command=selectDirectory)
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=300)
    
    progress(progress_bar)
    saved = Button(canvas, text="Salvar", command=save)
    
    styleSheet(text, button1)
    styleSheet(txt_dir, saved)

    text.place(x=220, y=120)
    button1.place(x=220, y=160)

    txt_dir.place(x=220, y=200)
    diretory.place(x=310, y=200)
    saved.place(x=360, y=280)

    progress_bar.place(x=250, y=450)


    if isOk():
        txt_finish.place(x=260, y=400)

    canvas.bind('<Configure>', resize_image)

    return window
