import pandas


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

    return morse_code_string


def morse_to_text(user_input):
    morse_dict = {row.code: row.letter for (index,row) in data.iterrows()}
    morse_dict[" "] = " "
    morse_input_list = user_input.split(" ")
    tran_list = [morse_dict[char] for char in morse_input_list]
    trans_string = "".join(tran_list)
    return trans_string


def translate(user_input):
    if is_mores_code(user_input):
        return morse_to_text(user_input)
    else:
        return text_to_morse(user_input)


continue_translating = True

while continue_translating:
    user_word = input("What would you like to translate? ").lower()
    continue_translating = end_loop(user_word)
    if continue_translating:
        result = translate(user_word)
        print(f"Translated: {result}")
print("\nThank you for using Morse Code Translator")


