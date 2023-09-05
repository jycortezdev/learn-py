# Collatz Sequence

def userInput():
    while True:
        try:
            print('Please enter an integer:')
            response = int(input())
            break
        except ValueError:
            print('Please enter a valid integer.')
    return response

def collatz(number):
    print(number)
    if(number % 2 == 0):        
        number = number // 2
        if(number == 1):
            return print(number)
        collatz(number)
    else:
        number = ((number*3)+1)
        collatz(number)

number = userInput()
collatz(number)