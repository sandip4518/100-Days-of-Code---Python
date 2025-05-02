import random
import hangman_art
import hangman_words

# 1. Import logo and print it
print(hangman_art.logo)

# 2. Get random word from word list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6
guessed_letters = []
display = ["_"] * word_length
game_over = False

print(f"Word to guess: {' '.join(display)}")

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # 3. Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    # 4. Check if guess is in word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

    print(f"\nWord to guess: {' '.join(display)}")
    print(hangman_art.stages[lives])

    # 5. Win/Lose condition
    if "_" not in display:
        print("**************************** YOU WIN ****************************")
        game_over = True
    elif lives == 0:
        print("*********************** YOU LOSE ***********************")
        print(f"The correct word was: '{chosen_word}'")
        game_over = True
