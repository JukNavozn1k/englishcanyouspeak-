import tkinter as tk

def ans_btn():
    # Function to execute when "Plug In" button is clicked
    print("Plugged In")

def transl_btn():
    # Function to execute when "Plug Out" button is clicked
    print("Plugged Out")

# Create main window
root = tk.Tk()

# Set window size
root.geometry("400x400")

font = ("Arial",16)

# Disable window resizing
#root.resizable(False, False)

# Create label with larger font and place in grid
label = tk.Label(root, text="<current word here>", font=font)
label.grid(row=0, column=1)


# Create label with larger font and place in grid
label = tk.Label(root, text="Enter word:", font=font)
label.grid(row=1, column=0)

# Create text box with larger font and place in grid
text_box = tk.Entry(root, font=font)
text_box.grid(row=1, column=1)

# Create "Plug In" button and place in grid
plug_in_button = tk.Button(root, text="Answer", command=ans_btn,font=font,width=10)
plug_in_button.grid(row=2, column=0)

# Create "Plug Out" button and place in grid
plug_out_button = tk.Button(root, text="Translate", command=transl_btn,font=font,width=10)
plug_out_button.grid(row=2, column=1)

# Start main loop
root.mainloop()
