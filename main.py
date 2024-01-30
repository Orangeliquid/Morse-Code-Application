from utility_functions import text_to_morse, morse_to_text, play_morse_music, clear_screen
import time
import pyperclip

is_true = True
while is_true:
    clear_screen()
    print("Welcome to the Morse Code App. \nThis app can accomplish a few tasks!")
    print("1. Convert Text to Morse Code. \n2. Convert Morse Code to Text. \n3. Audibly Play Morse Code. "
          "\n4. Exit Program")

    start_input = input("Enter Your Choice(1-4): ")

    # Takes text input from user and converts it to Morse Code
    if start_input == "1":
        clear_screen()
        print("Please enter text with the following constraints: "
              "\nLetters: A-Z \nNumbers: 0-9 \nPunctuation: '. , ? \  ! / ( ) & : ; = + - _ \ $ @ ")
        text_input = input("Enter your message in text: ").upper()
        morse_return = text_to_morse(text_input)

        if len(morse_return) == 0:
            time.sleep(1.5)
            continue
        else:
            print(f"\nMorse Code from Input: {morse_return}")
            clipboard_question = input("\nWould You Like to Store Morse in Clipboard?(Y?N): ").upper()
            time.sleep(1)
            if clipboard_question == "Y":
                pyperclip.copy(morse_return)
                print("Copied to Clipboard!")

            audible_morse_question = input("Would You Like to Hear the Morse Code?(Y?N): ").upper()
            if audible_morse_question == 'Y':
                print(f"\nMorse Code from Input: {morse_return}")
                play_morse_music(text_input)
            else:
                time.sleep(1.5)

    # Takes the Morse Code from Clipboard or input and converts it to Text
    elif start_input == "2":
        clear_screen()
        print("Please enter text with the following constraints: "
              "\nOnly dots and dashes (. -) "
              "\nSeparate characters by one space and words by three spaces ")

        reuse_morse = input("Would You Like to Use the Morse Code Saved in Your Clipboard?(Y?N): ").upper()
        if reuse_morse == "Y":
            print(f"Saved Morse Code in Use: {pyperclip.paste()}\n")
            morse_to_use = pyperclip.paste()
        else:
            morse_to_use = input("\nEnter Your Morse Code: ")

        invalid_chars = False
        for char in morse_to_use:
            if char not in ["-", ".", " "]:
                print("\nInvalid Input, Please Try Again.....")
                invalid_chars = True

        if not invalid_chars:
            text_return = morse_to_text(morse_to_use)
            print(f"\nDecoded Morse Code: {text_return}")
        time.sleep(4)

    # Plays Morse Code from Clipboard
    elif start_input == "3":
        clear_screen()
        print(f"Saved Morse Code to Text: {morse_to_text(pyperclip.paste())}")
        print(f"Saved Morse Code: {pyperclip.paste()}")
        print("Playing Now!")
        time.sleep(4)
        play_morse_music(morse_to_text(pyperclip.paste()))
        time.sleep(3)

    elif start_input == "4":
        clear_screen()
        is_true = False
        print("Come Again! \nExiting.....")
        time.sleep(3)

    # Ensures the starting prompt is followed correctly
    else:
        clear_screen()
        print("Please enter a valid choice (1-4)")
        time.sleep(3)
