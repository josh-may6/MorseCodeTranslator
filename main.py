import pandas
from tkinter import *
import pyperclip


def end_loop(entry_input):
    if entry_input == "don3":
        return False
    return True


data = pandas.read_csv('morse-alphabet.csv')


def is_mores_code(user_input):
    morse_code_indicators = {".", "-"}
    return any(char in morse_code_indicators for char in user_input)


def text_to_morse(user_input):
    morse_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    morse_code_list = [morse_dict[letter] for letter in user_input]
    morse_code_string = ' '.join(morse_code_list)
    output_entry.insert(0, morse_code_string)
    pyperclip.copy(morse_code_string)


def morse_to_text(user_input):
    morse_dict = {row.code: row.letter for (index,row) in data.iterrows()}
    morse_dict[" "] = " "
    morse_input_list = user_input.split(" ")
    tran_list = [morse_dict[char] for char in morse_input_list]
    trans_string = "".join(tran_list)
    output_entry.insert(0, trans_string)
    pyperclip.copy(trans_string)


def translate():
    user_input = input_entry.get().lower()
    output_entry.delete(0, END)
    if is_mores_code(user_input):
        return morse_to_text(user_input)
    else:
        return text_to_morse(user_input)


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
translate_button = Button(text="Translate", width=13, command=translate)  # Add function to button for translate funtion command=translate
translate_button.grid(column=2, row=1)

# Entries
input_entry = Entry(width=35)
input_entry.grid(column=1, row=1)

output_entry = Entry(width=35)
output_entry.grid(column=1, row=3)

window.mainloop()
