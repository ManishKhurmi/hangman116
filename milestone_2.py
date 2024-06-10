import random

word_list = ['mango', 'lychee', 'banana', 'blueberry', 'apple']

# randomly generated word 
word = random.choice(word_list)

# print variables
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {word}')

# Create user input 
guess = input('Enter a single letter:')
#guess

# check if the length of the input is 1 and the input is alphabetical
if len(guess) == 1:
    print('Good guess!')
if guess.isalpha() == True:
    print('Good guess!')
else: 
    print('Oops! That is not a valid input')
