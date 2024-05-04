import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 5
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while attempts > 0:
        # Prompt the player to guess the number
        guess = int(input(f"You have {attempts} attempts left. Guess the number: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            return
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
        
        # Decrement the number of attempts
        attempts -= 1
    
    # If the player runs out of attempts, they lose
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")

# Start the game
pass
guess_the_number()