# Hangman

A command-line Hangman game built in Python. Pick a category, guess letters one at a time, and try to reveal the word before running out of attempts.

## Features

- Multiple word categories (Animals, Programming, Countries)
- ASCII art hangman drawing that updates with each wrong guess
- Input validation (single letters only, no repeated guesses)
- Win/loss tracking across multiple rounds
- Replay option

## Project Structure

```
hangman/
├── words.py      # Word bank (categories and words)
└── hangman.py    # Game logic (main entry point)
```

## Requirements

- Python 3.6+
- No external libraries needed

## How to Run

```bash
python hangman.py
```

## How to Play

1. Choose a category by entering its number
2. Guess a letter by typing it and pressing Enter
3. Correct guesses reveal the letter in the word
4. Wrong guesses add a piece to the hangman drawing
5. You have 6 wrong guesses before you lose
6. Guess all the letters to win before running out of attempts
7. Choose to play again or exit

## Adding Your Own Words

Open `words.py` and add a new word to an existing category, or create a new category:

```python
"New Category": ["word1", "word2", "word3"],
```

## License

Free to use and modify.
