from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title('Kitties_Tomcats_Kittens')
window.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
new_image = load_image(url)
#_функция с параметром url (куда будет передаваться адрес url,
# будет возвращаться картинка, которую поместим в label)

if new_image:
    label.config(image=new_image)
    label.image = new_image
#_после получения new_image, проверяем, что new_image есть,
#_и выводим на метку, изменяя атрибут метки - image
#_label.image = new_image - нужен, чтобы не ушла картинка в мусор

window.mainloop()