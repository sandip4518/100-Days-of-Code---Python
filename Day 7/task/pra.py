import random
import hangman_art
import  hangman_words

print(hangman_art.logo)
chosen_word=random.choice(hangman_words.word_list)
print(chosen_word)
word_length=len(chosen_word)
lives=6
print("_ " * word_length)

display = ["_"] * word_length
guessed_letters = []

game_over = False

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed  {guess} letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
    print(" ".join(display))
    print(hangman_art.stages[lives])  # Show stage based on lives
    if "_" not in display:
        print("\n🎉 You won! The word was:", chosen_word)
        game_over = True
    elif lives == 0:
        print("\n💀 Game over! You lost.")
        print("The word was:", chosen_word)
        game_over = True

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.



