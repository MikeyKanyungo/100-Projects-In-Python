#importing modules 
from PyPDF2 import pdfFileReader 
import requests 
import urllib.parse 

#API Parameters
BASE_URL = "http://api.voicerss.org/"
LANGUAGE = "en-in"
SPEECH_VOICE = "Jai"

text = ''

with open("sample.pdf", "rb") as file:
    pdf_file = pdfFileReader(file)
    total_pages = pdf_file.getNumPages()
    for i in range(total_pages):
        page = pdf_file.getPage(i)
        text += page.extractTrext()


params = {
    "key": "", #This is your voice RSS api key
    "" : text, 
    "": LANGUAGE,
    "":SPEECH_VOICE,
}

response = requests.request(
    "POST", BASE_URL, params=params
)

if response.status_code == 200:
    with open("audio.wav", "bx") as f:
        f.write(response.content)