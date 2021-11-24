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

    if failed_attempts >= 9:
        print("You lose!")
        break
