import tkinter as tk
from voice_generator import * 
from DataLoad import *
import os
from random import randint
def resize_font(event):
    global font,root
        # Get the window size
    width = root.winfo_width()
    height = root.winfo_height()
    font_size = int(((1/3750)*width*height))
    # Print the window size
    #print(f'Window size: {width} x {height} | fsize =>  {font_size}')

    if font_size > 24: font_size = 24  # LIMIT MAX FONT SIZE
    elif font_size < 12: font_size = 12   
    else:
        font = ('Arial',font_size)
        word_lbl.config(font=font)
        enter_lbl.config(font=font)
        text_box.config(font=font)
        answer_button.config(font=font)
        translate_button.config(font=font)
        play_button.config(font=font)
   
def new_word():
    global idx,curr_lang
    idx = randint(0,len(words)-1)
    curr_lang = [0,2][randint(0,1)]
    word_lbl.config(text=f'{words[idx][curr_lang]}')
   
def ans_btn():
    # => сделать ебаную проврку на корректность
    new_word()

    pass
def transl_btn():
    global idx,curr_lang
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

# Create main window
root = tk.Tk()
root.title("englishcanyouspeak?")
# Set window size
root.geometry("400x150")

# Set minimum and maximum window size
root.minsize(300, 150)
#root.maxsize(500, 300)


font = ("Arial",16)
# загрузка слов с сервера, в случае их отсутствия
if not os.path.exists('words.json'):
    print('Data file not founc =( ')
    print('Starting download data...')
    get_words()


data = load_words()
words = None

print('Words loaded!')
for key in data:
    words = data[key]
    break
idx = randint(0,len(words)-1)
curr_lang = [0,2][randint(0,1)]
# Create label with larger font and place in grid
word_lbl = tk.Label(root, text=f'{words[idx][curr_lang]}', font=font,width=13)
word_lbl.grid(row=0, column=1,sticky='ew')


# Create label with larger font and place in grid
enter_lbl = tk.Label(root, text="Enter word:", font=font)
enter_lbl.grid(row=1, column=0,sticky='EW')

# Create text box with larger font and place in grid
text_box = tk.Entry(root, font=font)
text_box.grid(row=1, column=1,sticky='EW')

# Create "Plug In" button and place in grid
answer_button = tk.Button(root, text="Answer", command=ans_btn,font=font)
answer_button.grid(row=2, column=0,sticky='NSEW')

# Create "Plug Out" button and place in grid
translate_button = tk.Button(root, text="Translate", command=transl_btn,font=font)
translate_button.grid(row=2, column=1,sticky='NSEW')


play_button = tk.Button(root, text="Play sound", command=play_btn,font=font)
play_button.grid(row=2, column=2,sticky='NSEW')



# Configure the last row to have a non-zero weight
#root.grid_rowconfigure(2, weight=1)

# Configure the first column to have a non-zero weight
#root.grid_columnconfigure(1, weight=1)





#root.bind('<Configure>', resize_font) 
# Start main loop


root.mainloop()
