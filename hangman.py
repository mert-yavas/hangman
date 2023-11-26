import random
import string
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
print(logo)
lowercase_letters = list(string.ascii_lowercase)

# Initialize display list with blanks
display = ["_" for _ in range(len(chosen_word))]
guessed_letters = []

while "_" in display:
    guess = input("Guess a letter: ").lower()

    # Validate the guessed letter
    if guess not in lowercase_letters:
        print("Please enter a valid letter.")
    else:
        if guess in guessed_letters:
            print(f"You've already guessed {guess}.")
        else:
            guessed_letters.append(guess)    

            # Check each letter in the chosen word
            for index, letter in enumerate(chosen_word):  
                if letter == guess:
                    display[index] = guess

            # Lose a life if guess is incorrect
            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                print(stages[lives])
                if lives == 0:
                    print(f"You Lose. The correct word is {chosen_word}")
                    break

        # Show current state of the word
        print(" ".join(display)) 

    
    

