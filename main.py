# This is a sample Python script.


import random

numberTOGuess = random.randint(1, 10)

if __name__ == '__main__':
    print('Pick a number between 1 and 10')
    guessedNumber = int(input())
    while numberTOGuess != guessedNumber:
        print('Incorrect! Try again!')
        guessedNumber = int(input())
    print('You got it!')
