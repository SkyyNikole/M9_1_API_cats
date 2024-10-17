from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO


Allowed_tags = ['psychedelic', 'play', 'black', 'fight', 'jump', 'lazy', 'newyear', 'poptart', 'relax', 'programmer']
#_создаем список для Combobox

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
#_берем из combobox - вместо tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image = img)
        label.pack()
        label.image = img  # Сохраняем ссылку на изображение


def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x520")

#_tag_entry = Entry(window)
#_tag_entry.pack()
#_после создания Combobox - убираем

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = 'https://cataas.com/cat'

tag_label = Label(window, text = 'Выбери tag')
tag_label.pack()
tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_btn = Button(window, text='Загрузить по тегу', command = open_new_window)
load_btn.pack()
#_переместили кнопку под Combobox (была под entry)
window.mainloop()

