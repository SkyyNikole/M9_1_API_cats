from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


window = Tk()
window.title('Cats and Kittens')
window.geometry(f'500x400+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-200}')
window.iconbitmap('black_cat.ico')

url = 'https://cataas.com/cat'
#2_переменная со ссылкой на image с сайта
img = get_cat(url)
#3_в переменную img помещаяем функцию с параметром url, который она получит

label = Label()
#1_закинем сюда image c сайта
label.pack()



window.mainloop()