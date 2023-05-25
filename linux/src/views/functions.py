import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from extract.extract import extText as ext
from extract.extract import saveAudio

def progress(p_bar):
    global progress_bar
    progress_bar = p_bar


def selectDirectory():
    global dir
    dir = filedialog.askdirectory()
    print(dir)

def save():
    if dir:
        status = saveAudio(dir, progress_bar)
        if status == False:
            error(True)
        else:
            finish()



def intoFile():
    global file
    file = filedialog.askopenfilename()

    if file:
        print("extraindo texto")
        ext(file)
    

def resize_image(event, label, image):
    width, height = event.width, event.height
    resized_image = image.resize((1000, 700), Image.Resampling.LANCZOS)
    resized_photo = ImageTk.PhotoImage(resized_image)
    label.config(image=resized_photo)
    label.image = resized_photo


def error(e = None):
    if e == "tentativas" or e == True:
        error = tk.Tk()
        error.title("Error")
        
        txt_error = tk.Label(error, text="Erro: Seus usos diários acabaram! \n Tente amanhã")
        txt_error.pack()

        error.mainloop()

        return False
    else:
        return True


def finish():
    global finished
    finished = True


def isOk():
    try:
        if finished:
            return True
        else:
            return False
    except:
        return False