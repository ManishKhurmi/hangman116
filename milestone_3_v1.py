# While Loop Example
N = 3
Sum = 0
  
# This loop will run forever 
while True: 
    Sum += N 
    N -= 1
      
    # the below condition will tell 
    # the loop to stop 
    if N == 0: 
        break
          
print(f"Sum of First 10 Numbers is {Sum}")


##################################################################################################################################
# While loop to iteratively check if the guess is in the word 
while True: 
    
    guess = input('Guess a Letter:')

    if len(guess) == 1 and guess.isalpha() == True:
        print('Good guess!')
        break
    else: 
        print('Invalid letter. Please, enter a single alphabetical character')

# Check whether the guess is in the word 
if guess in random_word:
    print(f'Good guess! {guess} is in the word')
else:
    print(f'Sorry, {guess} is not in the word')

##################################################################################################################################

##################################################################################################################################
import random

word_list = ['mango', 'lychee', 'banana', 'blueberry', 'apple']

# randomly generated word 
random_word = random.choice(word_list)

# print variables
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {random_word}')
##################################################################################################################################

# Create functions to run the checks 
random_word

def check_guess(guess):
    '''
    This function checks if the guess is in the randomly generated word.
    '''
    guess = guess.lower()
    if guess in random_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word')

#test function
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


#################################################################
#################################################################
