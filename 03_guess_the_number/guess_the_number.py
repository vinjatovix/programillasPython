'''
Write a program with an infinite loop and a list of numbers. 
Each time through the loop the program should ask the user to guess a number (or type q to quit). 
If they type q, the program should end. 
Otherwise, 
it should tell them whether or not they successfully guessed a number in the list or not.

'''

import random


def guess_the_number():
    '''
    This program asks the user to guess a number between 0 and 10
    '''
    play = True
    while play:
        n = random.randint(0, 10)
        h = input('Guess the number or type \'q\' for leave:\r\n')

        # This checks if the user wanna leave
        if h.lower() == 'q':
            print('Goodbye!')
            break

        else:
            # this validates and check the input
            try:
                h = int(h)
                if h == n:
                    print('You Win!\r\n')
                else:
                    print('You loose...\r\n')

            except:
                print('That\'s not a valid number')


guess_the_number()
