# Milestone 2: Create the variables for the game 
import random

word_list = ['mango', 'lychee', 'banana', 'blueberry', 'apple']

# randomly generated word 
random_word = random.choice(word_list)

# print variables
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {random_word}')

# Create user input 
#guess = input('Enter a single letter:')
#guess

# Testing the user input
#guess = 'a' 

# check if the length of the input is 1 and the input is alphabetical
def check_user_guess(guess):
    if len(guess) == 1 and guess.isalpha() == True:
        print('Good guess!')
    else: 
        print('Oops! That is not a valid input')

#check_user_guess(guess)





