import tkinter as tk
from voice_generator import * 
from DataLoad import *
import os
from random import randint
import re
from getSyns import *
# функция, которая масштабирует шрифт, когда изменяются размеры окна
def resize_font(event):
    global font,root
    # получаем размер окна
    width = root.winfo_width()
    height = root.winfo_height()
    font_size = int(((1/30000)*width*height))
    #print(f'Window size: {width} x {height} | fsize =>  {font_size}') 
    # Ограничения на максимальный и минимальный размер шрифта
    if font_size > 20: font_size = 20
    elif font_size < 15: font_size = 15
    else:
        font = ('Arial',font_size)
        word_lbl.config(font=font)
        enter_lbl.config(font=font)
        text_box.config(font=font)
        answer_button.config(font=font)
        translate_button.config(font=font)
        play_button.config(font=font)
        listbox.config(font=font)
        update_button.config(font=font)

def upd_words():
    global selected_themes
    tmp =  get_selection()
    if len(tmp) > 0: 
        selected_themes = tmp
        new_word()
    else: print('Please, choose some themes')

# функция, которая возвращает список выбранных элементов из listbox
def get_selection():
    selection = [listbox.get(idx) for idx in listbox.curselection()]
    return selection
# функция, которая возвращает следующее случайное слово
def new_word():
    global idx,curr_lang,theme_idx,selected_themes
    # data[selected_themes[randint(0,len(selected_themes)-1)]][idx][curr_lang]
    
    if len(selected_themes) > 0:
        theme_idx = randint(0,len(selected_themes)-1) 
        words = data[selected_themes[theme_idx]]
        idx = randint(0,len(words)-1)
        curr_lang = [0,2][randint(0,1)] 
        word_lbl.config(text=f'{words[idx][curr_lang]}')
        theme_lbl.config(text=f"Тема: {selected_themes[theme_idx]}")
    else: print('select themes')
   
def ans_btn():
    if len (selected_themes) > 0 :
       # data[selected_themes[theme_idx]][idx][0]
       flag = False
       if curr_lang == 0 :
        # data[selected_themes[theme_idx]][idx][0]
        tmp_word = trs(text_box.get(),0)
        if tmp_word in ENget_syns(data[selected_themes[theme_idx]][idx][0]): flag = True
       
       elif curr_lang == 2 : 
           if text_box.get() in ENget_syns(data[selected_themes[theme_idx]][idx][0]):
                flag = True
       if flag: 
           text_box.delete(0, tk.END)
           new_word()


def transl_btn():
    global idx,curr_lang
    words = data[selected_themes[theme_idx]]
    text_box.delete(0, tk.END)
    if curr_lang == 0: text_box.insert(0,words[idx][2])
    else: text_box.insert(0,words[idx][0])
def play_btn():
    global curr_lang
    text = word_lbl.cget("text")
    if curr_lang == 0:
        text = "The word is : " + text
        if len(text) >  0:  ENplay_text(text)
    else:
        text = "Текущее слово : " + text
        if len(text) >  0:  RUplay_text(text)

root = tk.Tk()
root.title("englishcanyouspeak?") # заголовок окна
root.geometry("1000x500") # размеры окна


root.minsize(width=900,height=200) # минимальные размеры окна
root.maxsize(height=500) # максимальные размеры окна


font = ("Arial",16) # начальный шрифт   


# загрузка слов с сервера, в случае их отсутствия
if not os.path.exists('words.json'):
    print('Data file not founc =( ')
    print('Starting download data...')
    get_words()


data = load_words() # загрузка слов из words.json
selected_themes = []
print('Words loaded!')
for key in data:
    selected_themes.append(key)
    break
idx = randint(0,len(data[selected_themes[0]])-1)
curr_lang = [0,2][randint(0,1)]
theme_idx = randint(0,len(selected_themes)-1) 


word_lbl = tk.Label(root, text=f'{data[selected_themes[theme_idx]][idx][curr_lang]}', font=font,width=30)
word_lbl.grid(row=2, column=0,sticky='ew')

enter_lbl = tk.Label(root, text=f"Enter word:", font=font)
enter_lbl.grid(row=1, column=0,sticky='EW')

theme_lbl = tk.Label(root, text=f"Тема: {selected_themes[theme_idx]}", font=font)
theme_lbl.grid(row=0, column=1,sticky='EW')

text_box = tk.Entry(root, font=font,width=30)
text_box.grid(row=1, column=1,sticky='EW')


answer_button = tk.Button(root, text="Answer", command=ans_btn,font=font)
answer_button.grid(row=2, column=1,sticky='NSEW')


translate_button = tk.Button(root, text="Translate", command=transl_btn,font=font)
translate_button.grid(row=2, column=2,sticky='NSEW')


play_button = tk.Button(root, text="Play sound", command=play_btn,font=font)
play_button.grid(row=2, column=3,sticky='NSEW')



update_button = tk.Button(root, text="Update Words", command=upd_words,font=font)
update_button.grid(row=2, column=4,sticky='NSEW')

root.bind('<Configure>', resize_font)  # отслеживание изменения размера окна
# Start main loop

themes = [theme for theme in data]
# Create a Listbox widget with MULTIPLE option
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE,font=font,width=35)

# Insert items into Listbox
for theme in themes:
    listbox.insert(tk.END, theme)
listbox.selection_set(0)
listbox.grid(row=0,sticky='EW')



# Автозаполнение
root.grid_rowconfigure(0, weight=1) # автозаполнение по рядам
root.grid_columnconfigure(0, weight=1) # автозаполнение по столбцам


root.mainloop()
