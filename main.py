# Number Guessing Game
# The computer generates a random number between 1 and 100.
# The user is prompted to guess the number. If incorrect
# the user is told their number is either too low or too high.
# The user only gets 6 chances to guess the number before they lose.

import random

while (True):
    
    number = random.randint(0, 100)
    counter = 6
    print('Guess a number between 0 and 100.')
    print('You have 6 chances to guess the correct number.')

    while(True):
        if counter == 0:
            print('You ran out of guesses.')
            break
            
        guess = int(input("Input your guess: "))
        counter -= 1
        if guess == number:
            print('You are correct.')
            break
        elif guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')

    again = input('Play again? Enter y/n: ')
    if again == 'n':
        break
