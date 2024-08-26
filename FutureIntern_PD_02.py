import random

def number_guessing_game():
    while True:
        target_number = random.randint(1, 100)
        guess = None
        
        print("Hii Player, Welcome to the Number Guessing Game!")
        print("Right now I'm thinking of a number between 1 and 100. Can you guess what it is?")
        
        while guess != target_number:
            guess = int(input("Enter your guess: "))
            
            if guess > target_number and guess <= target_number + 10:
                print("You are very close! Guess a bit lower.")
            elif guess < target_number and guess >= target_number - 10:
                print("You are very close! Guess a bit higher.")
            elif guess < target_number:
                print("You are too low! Try again.")
            elif guess > target_number:
                print("You are too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number: {target_number}")
        
        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        
        if play_again == 'n':
            print("Thank you! We will be waiting for you till the next time.")
            break
        elif play_again == 'y':
            print("Starting a new game...")
        else:
            print("Invalid input. Exiting the game.")
            break

number_guessing_game()
