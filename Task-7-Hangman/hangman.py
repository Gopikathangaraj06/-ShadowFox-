import random

words = {
    "python": "A programming language",
    "biology": "Study of living organisms",
    "cloud": "Internet-based computing",
    "git": "Version control system"
}

word, hint = random.choice(list(words.items()))
guessed_letters = []
tries = 6

stages = [
    "",
    " O ",
    " O \n | ",
    " O \n/| ",
    " O \n/|\\",
    " O \n/|\\\n/ ",
    " O \n/|\\\n/ \\"
]

print("🎮 Welcome to Hangman!")
print("Hint:", hint)

while tries > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print(stages[6 - tries])

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess! Tries left:", tries)
else:
    print("❌ You lost! The word was:", word)
