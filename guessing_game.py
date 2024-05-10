import random

#We want to create guessing number game 
def play_game():
    rangNums0 = 1
    rangNums1 = 10
    MaxGuessingNumbers = 7
    #The number pc will generate 
    PcGuessingNumber = random.randint(rangNums0, rangNums1)

    guessesCounter = 0
    while guessesCounter < MaxGuessingNumbers:
        PlayersGuess = int(input("Guess A number Between {} and {} :".format(rangNums0, rangNums1)))
        if PlayersGuess == PcGuessingNumber:
            print("Congratulations! You Guessed the number in {} attemps".format(guessesCounter))    
        elif PlayersGuess < PcGuessingNumber:
            print("too low, try again! you have {} more attempts.".format(MaxGuessingNumbers))
        else:
            print("too high, try again! you have {} more attempts".format(MaxGuessingNumbers))    
        guessesCounter += 1
        
    if PlayersGuess == MaxGuessingNumbers:
        print("Sorry, you ran out of guess, The number was {}".format(PcGuessingNumber))
    

play_game()
    