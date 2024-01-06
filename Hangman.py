# This is a sample Python script.
import sys
from random import randint, choice


def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed.lower() in old_letters_guessed or len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_guessed.sort()
        print('X')
        print(' -> '.join(old_letters_guessed))
        letter_guessed = input("Guess a letter:")
        return try_update_letter_guessed(letter_guessed, old_letters_guessed)


def show_hidden_word(secret_word, old_letters_guessed):
    word_guessed = ''
    for letter in range(0, len(secret_word)):
        if secret_word[letter] in old_letters_guessed:
            word_guessed = word_guessed + secret_word[letter]
        else:
            word_guessed = word_guessed + '_'
        if letter < len(secret_word) - 1:
            word_guessed = word_guessed + ' '

    print(word_guessed)


def check_win(secret_word, old_letters_guessed):
    for letter in range(0, len(secret_word)):
        if not (secret_word[letter] in old_letters_guessed):
            return False
    return True


def choose_word(file_path, index):
    f = open(file_path, "r")
    word_list = [x for x in f.read().split()]
    index = (index - 1) % len(word_list)
    return word_list[index]


def open_game():
    open_sentence = "Welcome to the game Hangman\n"

    hangman_design = "  _    _                                         \n" \
                     " | |  | |                                        \n" \
                     " | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n" \
                     " |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n" \
                     " | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n" \
                     " |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n" \
                     "                      __/ |                      \n" \
                     "                     |___/"

    HANGMAN_PHOTOS = {
        'picture1': """x-------x
    """,

        'picture2': """x-------x
|
|
|
|
|
    """,

        'picture3': """x-------x
|       |
|       0
|
|
|
    """,

        'picture4': """x-------x
|       |
|       0
|       |
|
|
    """,

        'picture5': """x-------x
|       |
|       0
|      /|\\
|
|
    """,

        'picture6': """x-------x
|       |
|       0
|      /|\\
|      /
|
    """,

        'picture7': """x-------x
|       |
|       0
|      /|\\
|      / \\
|
    """
    }

    def print_hangman(num_of_tries):
        pic = 'picture{}'.format(num_of_tries)
        print(HANGMAN_PHOTOS[pic])

    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        # file_path = input
        file_path = 'words.txt'

        index = int(input("Enter the index for the secret word: "))
        secret_word = choose_word(file_path, index)
        old_letters_guessed = []

        MAX_TRIES = 6
        num_of_tries = 0
        print_hangman(num_of_tries + 1)
        show_hidden_word(secret_word, old_letters_guessed)

        # Main game loop
        while num_of_tries < 6:
            user_input = input("Guess a letter:")
            if try_update_letter_guessed(user_input, old_letters_guessed):
                if user_input not in secret_word:
                    num_of_tries += 1
                    print_hangman(num_of_tries + 1)
                else:
                    if check_win(secret_word, old_letters_guessed):
                        print("Win")
                        sys.exit()
            show_hidden_word(secret_word, old_letters_guessed)

        print("Lose")
        sys.exit()
