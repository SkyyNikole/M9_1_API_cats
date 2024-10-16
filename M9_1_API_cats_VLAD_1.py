from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title('Cats and Kittens')
window.geometry(f'500x400+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-200}')
window.iconbitmap('black_cat.ico')

window.mainloop()