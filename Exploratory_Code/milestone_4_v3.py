# For testing: 
import milestone_2 as milestone_2
# Giving values to the parameters 
word_list = milestone_2.word_list
word = milestone_2.random_word
 
print(f'This is my list of words: {word_list}')
print(f'This is the randomly generated word: {word}')

# ['mango', 'lychee', 'banana', 'blueberry', 'apple']
####################################################################################################################################
import random 

 # Task 1 
class Hangman:
    # Task 1
    def __init__(self, word_list, num_lives):
      
        self.word = random.choice(word_list) # random word picked from word_list 
        self.word_guessed = word_guessed # a list of letters of the word with a '_' if the letter is not guessed
        # create the logic for each variable base
        self.num_letters = word_guessed.count('_') # the number of UNIQUE letters not guessed yet 
        self.num_lives = num_lives # the number of lives the player has at the start of the game 
        self.word_list = word_list # e.g. ['mango', 'lychee', 'banana', 'blueberry', 'apple']
        self.list_of_guesses = [] # a list of guesses that have already been tried 


    # Task 1
    def create_word_guessed(word):
        '''
        Creates the word_guessed list 

        Example:
            For the word 'apple' then word_guessed = ['_', '_', '_', '_', '_']
        '''
        word_guessed = []
        for i in word: 
            word_guessed.append('_')
        return word_guessed
    # Task 1 
    def updates_word_guessed(guess):
        '''
        Updates the word_guessed list with the users guess

        Example:
            For the word 'apple' and guess = 'p' then ['_', 'p', 'p', '_', '_']
        
        '''
        position = [pos for pos, char in enumerate(word) if char == guess ] # finds the position of the letter in the word 
        for i in position: 
            word_guessed[i] = guess 
        return word_guessed

    # Task 2
    def check_guess(guess):
        '''
        This function checks if the guess is in the randomly generated word.
        '''
        guess = guess.lower() # converts the guess into a lowercase
        if guess in word:
            print(f'Good guess! {guess} is in the word')
    # Task 2
    def ask_for_input():
        '''
        Asks for user their guess and prints a message on the outcome.
        '''
        while True: 
            guess = input('Guess a Letter:')
            
            if len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character')
            if guess.isalpha() is False: #if the guess is not a single alphabetical character
                print('Invalid letter. Please, enter a single alphabetical character')
            elif guess in list_of_guesses:
                print('You already tried that letter!')
            else: 
                check_guess(guess)
    
    
# The following is to create word_guessed 
def create_word_guessed(word):
    '''
    Creates the word_guessed list 

    Example:
        For the word 'apple' then word_guessed = ['_', '_', '_', '_', '_']
    '''
    word_guessed = []
    for i in word: 
        word_guessed.append('_')
    return word_guessed

def updates_word_guessed(guess):
    '''
    Updates the word_guessed list with the users guess

    Example:
        For the word 'apple' and guess = 'p' then ['_', 'p', 'p', '_', '_']
    
    '''
    position = [pos for pos, char in enumerate(word) if char == guess ] # finds the position of the letter in the word 
    for i in position: 
        word_guessed[i] = guess 
    return word_guessed

word = 'apple'
guess = 'p'

# Testing create_word_guessed()
word_guessed = create_word_guessed(word)
word_guessed

# Testing word_guessed_updated()
word_guessed_updated = updates_word_guessed(guess)
word_guessed_updated


################################################################################################################
################################### SCRATCH WORK ###############################################################
################################################################################################################


# Creating the logic for word_guessed

# creating word_guessed list ['_', '_', '_', '_', '_']
word = 'apple'
word_guessed = []

for i in word: 
    word_guessed.append('_')
word_guessed

guess = 'p'

# Position of where to update 'p' i.e. covers the case of multiple characters 
    # iterate through the tuple pairs created by enumerate word to return the position conditional on if the character matches the users guess       
position = [pos for pos, char in enumerate(word) if char == guess ] 
# the guess 'p' had positions [1, 2] in 'apple'
position

# update list word_guessed for 'p'
for i in position: 
    word_guessed[i] = guess 

word_guessed

# Using the above, define a function that helps to create the word_guessed variable.

def create_word_guessed(word):
    word_guessed = []
    for i in word: 
        word_guessed.append('_')
    return word_guessed


word = 'apples'
word_guessed = create_word_guessed(word)
word_guessed

def updates_word_guessed(guess):
    
    for i in position: 
        word_guessed[i] = guess 
    return word_guessed

guess = 'p'

new_word_guessed = updates_word_guessed(guess)
new_word_guessed.count('_')



