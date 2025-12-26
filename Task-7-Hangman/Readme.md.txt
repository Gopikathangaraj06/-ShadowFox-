# Hangman Game – Intermediate Task

## Objective
To implement a word-guessing game using Python that includes visual progress,
hints, and user interaction.

## Description
This project is a Python-based implementation of the classic Hangman game.
The program randomly selects a word along with a hint and allows the user
to guess the word one letter at a time.

The player has a limited number of attempts. With each incorrect guess,
the hangman figure is progressively displayed using ASCII art. The game
ends when the player either successfully guesses the word or runs out of
attempts.

## Features
- Random word selection
- Hint system to assist the player
- Visual progress using ASCII hangman stages
- Input validation to prevent repeated guesses
- Clear win and lose conditions

## Concepts Used
- Dictionaries
- Lists
- Loops (`while`, `for`)
- Conditional statements (`if-else`)
- User input handling
- String manipulation
- Random module

## How the Game Works
1. A word and its hint are randomly selected from a dictionary.
2. The hint is displayed to the user.
3. The user guesses one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses reduce the number of remaining attempts and update
   the hangman visual.
6. The game continues until the word is fully guessed or all attempts are used.

## Tools Used
- Python
- VS Code

## Conclusion
This task helped in understanding how to combine multiple Python concepts
to build a complete interactive program. It strengthened logical thinking,
loop control, and user interaction handling.
