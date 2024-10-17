from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def out_pro():
    window.destroy()

list_of_tags_for_cats = ['black', 'Maine coon', 'programmer', 'cat_winston', 'spy']


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
    tag = tags_combobox.get()
#_9.1 _ получаем tag из entry из .get() и привязываем объект tag_combobox
#_10.2_убираем и добавляем
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else f'https://cataas.com/cat'
#_9.2_новые url с tag, если есть tag, a иначе - без /tag
    #_img = get_cat(url) - после 9.2 изменяем на 9.3 c новым параметром для url с tag
    img = get_cat(url_with_tag)
# 3_в переменную img помещаяем функцию с параметром url,
# на который она получит картинку с сайта
# _5.1_переносим вызов функции get_cat() получения нов изобр
#_нажим кнопку и вызываем get_new_img(), внутри которой
# вызывается get_cat(url) и в img запоминается картинка по url
    if img:
        new_window = Toplevel()
        new_window.iconbitmap('black_cat.ico')
        label = Label(new_window, image=img)
        #_label.config(image=img) - убрали, тк теперь картинка сразу открывается в нов окне
        label.image = img
        label.pack()
#_6.1_изменяем и сохраняем
#_8.1_при вызове get_new_img(), где мы должны создать Toplevel окно,
#_и в него поместить label

window = Tk()
window.title('Cats and Kittens')
window.geometry(f'500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}')
window.iconbitmap('black_cat.ico')

#_url = 'https://cataas.com/cat' - после 9.1 не нужно
#2_переменная со ссылкой на image с сайта

#_8 label = Label(window) переносим в Toplevel окно
#_6 изменяем - теперь в нем изначально нет изображения - см. 6.1
#_1 label = Label(window, image=img)
#1_закинем сюда image c сайта
#_label.pack() - тоже перенесли в 8.1

#_entry = Entry(window)
#_entry.pack()
#_9 создаем entry и получаем из entry инфу в 9.1
#10_после выбора по тегам убрали entry

tag_label = ttk.Label(window, text='Choose_your_Cat_by_Tag:')
tag_label.pack()

tags_combobox = ttk.Combobox(window, values=list_of_tags_for_cats)
tags_combobox.pack()
#_10.1_combobox и список тэгов


main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = 'File', menu=file_menu)
file_menu.add_command(label = 'Get_A_Cat', command = get_new_img)
file_menu.add_separator()
file_menu.add_command(label = 'No_More_Cats_For_Me - Quit', command = out_pro)



#_load_btn = Button(window, text='GetCat_by_Click', command=get_new_img)
#_load_btn.pack()
#_7 вместо кнопки делаем меню

window.mainloop()