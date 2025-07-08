#!/usr/bin/env python3
import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # Check nt for windows execution, otherwise assume linux

def guess_prompt():
    while True:
        response = input("Guess: ").upper()
        if len(response) == 5:
            return response
        else:
            print("Invalid input. Please enter exactly 5 characters.")

def ask_play_again():
    while True:
        response = input("Play again? (y/n): ").strip().lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Colors
default_color = "\033[0m"
correct_color = "\033[92m"
incorrect_color = "\033[91m"
misplaced_color = "\033[93m"

WORD_LIST_PATH = "/usr/share/wordminal/word-list.txt"  # maybe should do try catch in case it is being run from pycharm instead?

title = " __        __            _           _             _ \n \ \      / /__  _ __ __| |_ __ ___ (_)_ __   __ _| |\n  \ \ /\ / / _ \| '__/ _` | '_ ` _ \| | '_ \ / _` | |\n   \ V  V / (_) | | | (_| | | | | | | | | | | (_| | |\n    \_/\_/ \___/|_|  \__,_|_| |_| |_|_|_| |_|\__,_|_|"

def main():
    playing = True
    won = False

    with open(WORD_LIST_PATH, "r") as file:
        words = file.read().splitlines()

    clear_terminal()
    while playing:
        rounds = 5  # Number of rounds to be played before a game over
        guess_list = []  # Store previous guesses
        current_round = 0

        # Choose a random word
        chosen_word = random.choice(words).upper()

        while current_round < rounds:
            clear_terminal()
            print(title + "\n\n\n\n")

            # Only display previous guesses if they exist
            if len(guess_list) > 0:
                for v in guess_list:
                    print(v)
                print(default_color + "\n\n")
            else:
                print("Welcome to Wordminal! Enter a 5 letter word below to begin.\n")

            print(f"Remaining Guesses: {rounds - current_round}\n")

            # Ask user for their guess
            guess = guess_prompt()

            # Increment round and initialize the colored guess to be stored
            current_round += 1
            colored_guess = ""
            # Check if the guess matches the chosen word
            if guess == chosen_word:
                won = True
                print(f"You won in {current_round} guesses!")
                playing = False
                break
            # Otherwise, check if letters are in the correct space, incorrect space, or do not exist.
            else:
                for i in range(len(chosen_word)):
                    # Correct
                    if chosen_word[i] == guess[i]:
                        colored_guess += correct_color + guess[i]
                    # Misplaced
                    elif guess[i] in chosen_word:
                        colored_guess += misplaced_color + guess[i]
                    # Incorrect
                    else:
                        colored_guess += incorrect_color + guess[i]

                guess_list.append(colored_guess + default_color)
                print(default_color)

        # After the game has ended, display result and ask for another round.
        clear_terminal()
        print(title + "\n\n\n\n")
        if won:
            print(f"Won in {current_round} guesses!")
        else:
            print("Ran out of guesses...\n")
            print(f'The word was: "{chosen_word}"\n')
        playing = ask_play_again()

    # Clear if the game has been stopped.
    clear_terminal()


if '__name__' == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()