import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of guesses to 0
num_guesses = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Loop until the user guesses the correct number
while True:
    # Get a guess from the user
    guess = int(input("Enter your guess: "))
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
