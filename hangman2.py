import random

# List of words for the game
word_list = ["python", "java", "javascript", "hangman", "programming", "computer", "developer", "algorithm"]

# List of hangman stages (6 incorrect guesses)
hangman_stages = [
    '''
       ------
       |    |
            |
            |
            |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
            |
            |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
       |    |
            |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
      /|    |
            |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
            |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
        -----
    ''',
    '''
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
        -----
    '''
]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the Hangman game
def hangman():
    # Randomly choose a word from the list
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6  # Number of attempts a player has
    guessed_word = False

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    
    while attempts > 0 and not guessed_word:
        print(hangman_stages[6 - attempts])  # Show the current hangman drawing
        print("\n" + display_word(word, guessed_letters))  # Show the word with guessed letters
        print(f"You have {attempts} attempts remaining.")
        guess = input("Guess a letter: ").lower()
        
        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        # If the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # If the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Oops! The letter {guess} is not in the word.")
        
        # Check if the player has guessed all letters of the word
        if all(letter in guessed_letters for letter in word):
            guessed_word = True
            print(f"Congratulations! You've guessed the word: {word}")

    # If the player runs out of attempts
    if not guessed_word:
        print(f"\nSorry, you've run out of attempts. The word was: {word}")

# Start the game
if __name__ == "__main__":
    hangman()
