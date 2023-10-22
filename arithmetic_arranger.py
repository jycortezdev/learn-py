import re

#function that will check if the input is an integer
def is_char_value(value):
            try:
                is_numeric = value.isnumeric()
                if is_numeric == True:
                    return False
                elif value == '+' or value == '-':
                     return False
                else:
                     return True
            except ValueError:
                 print('the input is char is not allowed')

def arithmetic_arranger(problems):
    #get inputs
    split_all_chars = []
    flag = False

    for char in problems:
        splitted_char = char.split()
        split_all_chars.append(splitted_char)

        if flag == True:
         print('an illegal character was found.')
         break

        #examine if the splitted char contains a non-numeric character that is not '+' or '-'
        for item in splitted_char:

            if is_char_value(item) == True:
                print(item)
                flag = True
                break
            else:
                print(item)
        

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])