import PyPDF2
from gtts import *
import time
from src.views.functions import *

def extText(file):
    global text_pdf
    with open(file, 'rb') as file:
        text_pdf = ''   
        pdf_read = PyPDF2.PdfReader(file)

        for n_page in range(len(pdf_read.pages)):
            page = pdf_read.pages[n_page]
            text_pdf += page.extract_text()
        
        print('texto extraido')
        return text_pdf
    
def saveAudio(dir, progress_bar):
    language = "pt"
    output_file = str(dir) + "/myPDF.mp3"

    try:

        tts = gTTS(text=text_pdf, lang=language)
        
        progress_bar.start()
        tts.save(output_file)
        progress_bar.stop()
        
        time.sleep(1)

        print("Success")

    except gTTSError:
        progress_bar.stop()
        return False