import tkinter as tk
from voice_generator import * 
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
   

def ans_btn():
    # Function to execuvte when "Plug In" button is clicked
    print("Plugged In")

def transl_btn():
    # Function to execute when "Plug Out" button is clicked
    print("Plugged Out")
def play_btn():
    text = text_box.get()
    if len(text) >  0:  ENplay_text(text)
# Create main window
root = tk.Tk()
root.title("englishcanyouspeak?")
# Set window size
root.geometry("400x150")

# Set minimum and maximum window size
root.minsize(300, 150)
#root.maxsize(500, 300)


font = ("Arial",16)


# Create label with larger font and place in grid
word_lbl = tk.Label(root, text="<current word here>", font=font)
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
root.grid_rowconfigure(2, weight=1)

# Configure the first column to have a non-zero weight
root.grid_columnconfigure(1, weight=1)




root.bind('<Configure>', resize_font) 
# Start main loop
root.mainloop()
