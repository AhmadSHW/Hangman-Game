import random
from words import WORDS

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
]

def choose_category():
	categories = list(WORDS.keys())
	print("Choose a category:")
	for i , cat in enumerate(categories, start=1):
		print(f"{i}. {cat}")

	while True:
		choice = input("Category number: ").strip()
		if choice.isdigit() and 1<= int(choice) <= len(categories):
			return categories[int(choice) -1]
		print("Invalid choice, try again.")


def choose_word(category):
	return random.choice(WORDS[category])

def display_word(word, guessed_letters):
	return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_guess(guessed_letters):
	while True:
		guess = input("Guess a letter: ").strip().lower()
		if len(guess) != 1 or not guess.isalpha():
			print("Please enter a single letter.")
		elif guess in guessed_letters:
			print("You have already guessed that letter.")
		else:
			return guess


def play_round():
	category = choose_category()
	word = choose_word(category)

	guessed_letters = set()
	wrong_guesses = 0
	print(f"\nCategory: {category}")
	print(f"The word has {len(word)} letters.")

	while wrong_guesses < MAX_ATTEMPTS:
		print(HANGMAN_STAGES[wrong_guesses])
		print("Word:" + display_word(word, guessed_letters))
		print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_guesses}")

		guess = get_guess(guessed_letters)
		guessed_letters.add(guess)

		if guess in word:
			print("Correct!")
			if all(letter in guessed_letters for letter in word):
				print(f"\nYou won! The word was: {word}")
				return True
		else:
			wrong_guesses += 1
			print("Wrong guess!")

	print(HANGMAN_STAGES[wrong_guesses])
	print(f"\nYou lost! The word was: {word}")
	return False

def main():
	wins = 0
	losses = 0
	while True:
		print("=" * 40)
		print("HANGMAN")
		print("=" * 40)

		if play_round():
			wins += 1
		else:
			losses += 1

		print(f"\nScore -> Wins: {wins} | Losses: {losses}")
		again = input("\nPlay again? (y/n):").strip().lower()
		if again != "y":
			print("Goodbye!")
			break

if __name__ == "__main__":
	main()
