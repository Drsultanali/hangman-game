import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "random", "programming", "codealpha", "internship"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to play the Hangman game
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was '{word}'.")

# Start the game
play_hangman()
