from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

#_4 функция получаем картинку, вернули через return и запомнилась она в img (#_3)
def get_cat(url):
    get_bytes_img = requests.get(url)
#_4.1_отправляем запрос на сайт url и получаем ответ в виде картинки в битовом формате
    norm_img = BytesIO(get_bytes_img.content)
#_4.2_преобразовали и битового форм контент в норм картинку
    norm_img_opened = Image.open(norm_img)
#_4.3_открываем с помощью библ PIL
    img_tk = ImageTk.PhotoImage(norm_img_opened)
#_4.4_преобразуем для tkinter
    return img_tk
#_4.5_возвращаем на функцию


window = Tk()
window.title('Cats and Kittens')
window.geometry(f'500x400+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-200}')
window.iconbitmap('black_cat.ico')

url = 'https://cataas.com/cat'
#2_переменная со ссылкой на image с сайта
img = get_cat(url)
#3_в переменную img помещаяем функцию с параметром url, на который она получит картинку с сайта

label = Label(window, image = img)
#1_закинем сюда image c сайта
label.pack()

window.mainloop()