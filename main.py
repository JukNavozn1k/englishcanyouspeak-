import tkinter as tk

def resize_font(event):
    global font,root
        # Get the window size
    width = root.winfo_width()
    height = root.winfo_height()
    # Print the window size
    print(f'Window size: {width} x {height}')
    font_size = int(((1/5000)*width*height))
    if font_size > 24: font_size = 24  # LIMIT MAX FONT SIZE
    elif font_size < 12: font_size = 12
    else:
        font = ('Arial',font_size)
        label.config(font=font)
        text_box.config(font=font)
        answer_button.config(font=font)
        translate_button.config(font=font)
   

def ans_btn():
    # Function to execuvte when "Plug In" button is clicked
    print("Plugged In")

def transl_btn():
    # Function to execute when "Plug Out" button is clicked
    print("Plugged Out")

# Create main window
root = tk.Tk()
root.title("englishcanyouspeak?")
# Set window size
root.geometry("400x150")

# Set minimum and maximum window size
root.minsize(300, 150)
root.maxsize(500, 300)


font = ("Arial",16)


# Create label with larger font and place in grid
label = tk.Label(root, text="<current word here>", font=font)
label.grid(row=0, column=1,sticky='ew')


# Create label with larger font and place in grid
label = tk.Label(root, text="Enter word:", font=font)
label.grid(row=1, column=0,sticky='EW')

# Create text box with larger font and place in grid
text_box = tk.Entry(root, font=font)
text_box.grid(row=1, column=1,sticky='EW')

# Create "Plug In" button and place in grid
answer_button = tk.Button(root, text="Answer", command=ans_btn,font=font,width=10)
answer_button.grid(row=2, column=0,sticky='NSEW')

# Create "Plug Out" button and place in grid
translate_button = tk.Button(root, text="Translate", command=transl_btn,font=font,width=10)
translate_button.grid(row=2, column=1,sticky='NSEW')



# Configure the last row to have a non-zero weight
root.grid_rowconfigure(2, weight=1)

# Configure the first column to have a non-zero weight
root.grid_columnconfigure(0, weight=1)




root.bind('<Configure>', resize_font)
# Start main loop
root.mainloop()
