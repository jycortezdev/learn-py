# practicing loops

print('This program will only retry 3 times.')

i = 0 # set the index starting point

while i < 4:
    print('Can you guess my name correctly?')

    name = 'joshan'
    guessedName = input()
    if(guessedName !=name and i < 4):
        print('That is not my name!')
        i = i + 1
        if(i==4):
            print('you have ran out of guesses! Terminating program.')
            break
        else:
            print('retry attempt #' + str(i))
        print("let's try this again.")
    elif(guessedName == name):
        print('you have guessed correctly! My name is: ' + name)
        break