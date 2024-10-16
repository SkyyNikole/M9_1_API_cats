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
    norm_img_opened.thumbnail((500, 400))
#_4.3.1_изменяем размер под наше окно - размер указываем в виде кортежа
    img_tk = ImageTk.PhotoImage(norm_img_opened)
#_4.4_преобразуем для tkinter
    return img_tk
#_4.5_возвращаем на функцию


#_5_функц для кнопки - будем получать новую картику с котом
def get_new_img():
    img = get_cat(url)
# 3_в переменную img помещаяем функцию с параметром url,
# на который она получит картинку с сайта
# _5.1_переносим вызов функции get_cat() получения нов изобр
#_нажим кнопку и вызываем get_new_img(), внутри которой
# вызывается get_cat(url) и в img запоминается картинка по url
    if img:
        label.config(image=img)
        label.image = img
#_6.1_изменяем и сохраняем

window = Tk()
window.title('Cats and Kittens')
window.geometry(f'500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}')
window.iconbitmap('black_cat.ico')

url = 'https://cataas.com/cat'
#2_переменная со ссылкой на image с сайта

label = Label(window)
#_6 изменяем - теперь в нем изначально нет изображения - см. 6.1
#_1 label = Label(window, image=img)
#1_закинем сюда image c сайта
label.pack()

load_btn = Button(window, text='GetCat_by_Click', command=get_new_img)
load_btn.pack()

window.mainloop()