# This is a guess the numbner game.
import random

secretNumber = random.randint(1,20) #generates a random integer from 1 through 20
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input()) #cast the input as an integer.

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        print('You guessed correctly! The number I am thinking of is: '+ str(secretNumber))
        break #the program exits because the user guessed the correct number.

if guess == secretNumber:
    print('Good job! You guessed my number in  ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. the number I was thinking of was ' + str(secretNumber))
