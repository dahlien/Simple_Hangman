# simple_hangman.py
from random import randint

print("Welcome to Simple Hangman game! \nAll the words are names of programming languages. \nGood luck!")

words = ["python", "rust", "php", "kotlin", "perl", "ruby", "go"]
secret_word = words[(randint(0, (len(words)-1)))]
game_state = (len(secret_word) * "_")
print(game_state)
failed_attempts = 0

while True:
    guessed_letter = (input("Guess a letter: ").lower())
    if len(guessed_letter) != 1:
        print("Guess only one letter! \n")
    else:
        if not (ord(guessed_letter) >= 97 and ord(guessed_letter) <= 122):
            print("This character is not a letter! \n")
        else:
            if guessed_letter in secret_word:
                position = secret_word.index(guessed_letter)
                game_state = game_state[:position] + \
                    guessed_letter + game_state[position + 1:]
            else:
                failed_attempts += 1
            print(game_state)

            if "_" not in game_state:
                print("Congratulations, you won!")
                break

            print(f"Number of failed attempts: {failed_attempts} \n")

            if failed_attempts == 0:
                print("""







                ~~~~~~~
                """)
            elif failed_attempts == 1:
                print("""
                +
                |
                |
                |
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 2:
                print("""
                +---.
                |
                |
                |
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 3:
                print("""
                +---.
                |   |
                |
                |
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 4:
                print("""
                +---.
                |   |
                |   O
                |
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 5:
                print("""
                +---.
                |   |
                |   O
                |   |
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 6:
                print("""
                +---.
                |   |
                |   O
                | --|
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 7:
                print("""
                +---.
                |   |
                |   O
                | --|--
                |
                |
                ~~~~~~~
                """)
            elif failed_attempts == 8:
                print("""
                +---.
                |   |
                |   O
                | --|--
                |  /
                |
                ~~~~~~~
                """)
            elif failed_attempts == 9:
                print("""
                +---.
                |   |
                |   O
                | --|--
                |  / \\
                |
                ~~~~~~~
                """)
                print("You lose!")
                break
