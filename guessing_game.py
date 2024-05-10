import random

#We want to create guessing number game 
def play_game():
    print("Welcome to the Guessing Game!")
    rangNums0 = 1
    rangNums1 = 10
    MaxGuessingNumbers = 7
    #The number pc will generate 
    PcGuessingNumber = random.randint(rangNums0, rangNums1)

    guessesCounter = 0
    while guessesCounter < MaxGuessingNumbers:
        try:
            PlayersGuess = int(input("Guess A number Between {} and {} :".format(rangNums0, rangNums1)))
            guessesCounter += 1
            if PlayersGuess == PcGuessingNumber:
                print("Congratulations! You Guessed the number in {} attemps".format(guessesCounter)) 
                break     
            elif PlayersGuess < PcGuessingNumber:
                print("too low, try again! you have {} more attempts.".format(MaxGuessingNumbers - guessesCounter))
            else:
                print("too high, try again! you have {} more attempts".format(MaxGuessingNumbers - guessesCounter)) 
        except ValueError:
                print("Please enter a valid number.")
    if PlayersGuess != PcGuessingNumber:
        print("Sorry, you ran out of guesses. the number was {}".format(PcGuessingNumber))
          
    play_again = input("Do you want to play again? (yes/no): ") 
    if play_again.lower() == "yes":
       play_game()   
    else:
        print("Thanks for Playing") 

play_game()
    