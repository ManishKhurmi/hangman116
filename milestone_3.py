# Milestone 3: Check if the guessed character is in the word 
import milestone_2 as milestone_2

word_list = milestone_2.word_list
random_word = milestone_2.random_word


def check_guess(guess):
    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower()
    if guess in random_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word')

# Test check_guess
#check_guess('B')

def ask_for_input():
    '''
    Asks for user their guess and prints a message on the outcome.
    '''
    while True: 
        guess = input('Guess a Letter:')

        if len(guess) == 1 and guess.isalpha() == True:
            print('Good guess!')
            break
        else: 
            print('Invalid letter. Please, enter a single alphabetical character')

    # call the check_guess function outside of the while loop 
    check_guess(guess)
    
ask_for_input()
