from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Morse Code Translator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
telegraph_image = PhotoImage(file="key-telegraph-Morse-1860.jpg copy.png")
canvas.create_image(100, 100, image=telegraph_image)
canvas.grid(column=1, row=0)

# Labels
input_label = Label(text="Input")
input_label.grid(column=0, row=1)

output_label = Label(text="Output")
output_label.grid(column=0, row=3)

# Buttons
translate_button = Button(text="Translate", width=13)  # Add function to button for translate funtion command=translate
translate_button.grid(column=2, row=1)

add_button = Button(text="Add to Favorites", width=36)  # Add function for save responses command=save
add_button.grid(column=1, row=4)

# Entries
website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

window.mainloop()
