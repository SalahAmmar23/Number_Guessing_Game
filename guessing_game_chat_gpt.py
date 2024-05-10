import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    play_again = 'yes'
    min_attempts = float('inf')
    
    while play_again.lower() == 'yes':
        target_number = random.randint(1, 10)
        attempts = 0

        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                attempts += 1
                
                if guess == target_number:
                    print("Congratulations! You guessed the correct number!")
                    print(f"Number of attempts: {attempts}")
                    min_attempts = min(min_attempts, attempts)
                    break
                else:
                    if guess < target_number:
                        print("Too low! Try a higher number.")
                    else:
                        print("Too high! Try a lower number.")
            except ValueError:
                print("Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ")

    print(f"Minimum number of attempts in this session: {min_attempts}")

if __name__ == "__main__":
    guessing_game()
