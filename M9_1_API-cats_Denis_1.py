from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
#_делаем запрос по url и то, что вернется, положим в response
        response.raise_for_status()
#_для обработки исключений, если будет ошибка, мы ее получим здесь
        image_data = BytesIO(response.content)
#_обрабатываем полученное изображение в байтах
        image_got = Image.open(image_data)
#_полученное изображение открываем с помощью pillow
        image_got.thumbnail((600, 480), Image.Resampling.LANCZOS)
#_подгоняем размер - чтобы качество не страдало от изм размера
        return ImageTk.PhotoImage(image_got)
#_функция возвращает нам полученное изображение, которое мы положим
#_new_image = load_image(url), дальше положим label.config(image = new_image)
    except Exception as e:
        print(f'Произошла ошибка: {e}.')
        return None


def set_image():
    new_image = load_image(url)
    # _функция с параметром url (куда будет передаваться адрес url,
    # будет возвращаться картинка, которую поместим в label)

    if new_image:
        label.config(image = new_image)
        label.image = new_image
    # _после получения new_image, проверяем, что new_image есть,
    # _и выводим на метку, изменяя атрибут метки - image
    # _label.image = new_image - нужен, чтобы не ушла картинка в мусор


window = Tk()
window.title('Kitties_Tomcats_Kittens')
window.geometry('600x520')

label = Label(window)
label.pack()

update_button = Button(window, text='Обновить', command = set_image)
update_button.pack()

url = 'https://cataas.com/cat'

set_image()

window.mainloop()