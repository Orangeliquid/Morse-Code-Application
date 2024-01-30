import pygame
import time

# This file will contain all functions needed to run in the main.py.
# I like the idea of having a clean and short looking main.py

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',
}

# Initialize pygame sound and set dash/dot variables
pygame.mixer.init()
dash_loc = pygame.mixer.Sound("audio/dash.wav")
dot_loc = pygame.mixer.Sound("audio/dot.wav")


def text_to_morse(text):
    morse_string = ""
    morse_list = []
    unknown_char = []

    # Remove space from input and check for unknown characters
    for char in text.replace(" ", ""):
        if char not in MORSE_DICT.keys():
            unknown_char.append(char)

    if len(unknown_char) == 0:
        for char in text:
            if char == " ":
                morse_list.append(char)
            else:
                morse_list.append(MORSE_DICT[char])

        morse_string = " ".join(morse_list)
    else:
        print(f"\nError: {unknown_char} is not found in Morse Code dictionary.")

    return morse_string


def morse_to_text(morse_code):
    morse_in_text = ""

    # Reverse the MORSE_DICT so MORSE is the key and TEXT is the value
    reversed_morse_dict = {morse: char for char, morse in MORSE_DICT.items()}

    for word in morse_code.split("   "):
        letters = [reversed_morse_dict[letter] for letter in word.split(" ")]
        morse_in_text += "".join(letters)
        # adding a space between words
        morse_in_text += " "

    return morse_in_text


# Takes text and plays the morse code characters audibly
def play_morse_music(text):
    # print(morse)
    for char in text:
        if char == " ":
            time.sleep(0.6)
        else:
            get_char = MORSE_DICT.get(char.upper())
            for item in get_char:
                # print(f'The characters are {item}')
                if item == "-":
                    dash_loc.play()
                    pygame.time.wait(int(dash_loc.get_length() * 3000))
                elif item == ".":
                    dot_loc.play()
                    pygame.time.wait(int(dot_loc.get_length() * 2200))


# Clearing the system in pycharm is oddly difficult via code
# I have tried os.system('clear') and os.system('cls' if os.name == 'nt' else 'clear')
# This is my work-around to continue the app.
def clear_screen():
    print('\n' * 20)
